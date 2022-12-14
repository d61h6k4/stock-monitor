from altair import Chart, Axis, X, Y, Scale, datum, value, condition, Y2, Y2Datum, Text, layer
from dataclasses import dataclass
from datetime import datetime, timedelta
from pandas import DataFrame
from stock_monitor.models import Arbitrage


def arbitrage_strategy(arbitrage: Arbitrage) -> Arbitrage:
    target_history = arbitrage.target.history

    if not isinstance(arbitrage.buyer, str):
        buyer_history = arbitrage.buyer.history
        buyers_value = buyer_history.Close.values[-1]
    else:
        buyers_value = 0
        buyer_history = target_history
    final_offer_price = arbitrage.offer_price + arbitrage.additional_buyer_ratio * buyers_value
    last_date = target_history.Date.max()

    assert arbitrage.target.price_chart is not None, \
        "Arbitrage strategy appliable only to the already evaluated strategy"

    base = Chart(target_history).encode(X("Date:T", axis=Axis(title=None)))
    offer_line = base.mark_line(color="#ABCEE2", strokeDash=[1, 2]) \
        .encode(y=datum(final_offer_price))
    offer_line_text = offer_line.mark_text(color="#ABCEE2", dx=65, dy=7,
                                           text=f"Offer price = {final_offer_price:.1f}",
                                           fontSize=12) \
        .encode(x=value(0))

    yield_rule = base.mark_rule(color="#ABCEE2", ) \
        .transform_filter(f"year(datum.Date)=={last_date.year} && "
                          f"month(datum.Date)=={last_date.month - 1} && "
                          f"date(datum.Date)=={last_date.day}") \
        .encode(Y("Close:Q"),
                Y2Datum(
                    datum=final_offer_price))
    yield_rule_text = yield_rule.mark_text(color="#ABCEE2", angle=270, baseline="bottom", dx=50, fontSize=12) \
        .transform_calculate(spread=(final_offer_price - datum.Close) / datum.Close) \
        .encode(text=Text("spread:Q", format=".2%", formatType="number"))

    dates = []
    if arbitrage.expecting_closing < last_date + timedelta(days=10):
        dates.append(arbitrage.expecting_closing)
    else:
        dates.append(last_date + timedelta(days=10))
    texts = [f"Exp. closing {arbitrage.expecting_closing.date()}"]
    e_closing_rule = Chart(DataFrame({'Date': dates,
                                      'text': texts})).mark_rule(color="#ABCEE2", strokeDash=[1, 5]) \
        .encode(x="Date:T")
    e_closing_rule_text = e_closing_rule.mark_text(color="#ABCEE2", angle=270, baseline="bottom") \
        .encode(text="text:N")

    if isinstance(arbitrage.buyer, str):
        buyer_ticker_name = arbitrage.buyer
    else:
        buyer_ticker_name = arbitrage.buyer.ticker_name
    buyer_line = Chart(buyer_history).mark_line(stroke="#BEA1A5", strokeDash=[1, 5]) \
        .encode(X("Date:T", axis=Axis(title=None)),
                Y(
                    'Close:Q',
                    title=f'{buyer_ticker_name}',
                    scale=Scale(zero=False),
                )
                )
    chart = layer(buyer_line,
                  arbitrage.target.price_chart + offer_line + offer_line_text + yield_rule +
                  yield_rule_text + e_closing_rule + e_closing_rule_text) \
        .resolve_scale(y="independent")
    return chart
