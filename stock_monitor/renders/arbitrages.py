from altair import Chart, Axis, X, Y, Scale, datum, value, condition, Y2, Y2Datum, Text, layer
from datetime import datetime, timedelta
from pandas import DataFrame
from yfinance import Ticker


class Arbitrage:
    def __init__(self, target_ticker_name: str, buyer_ticker_name: str, offer_price: float,
                 additional_buyer_ratio: float,
                 expecting_closing: datetime, commentary: str, period: str, is_buyer_company: bool = True):
        self.period = period
        self.is_buyer_company = is_buyer_company
        self.target_ticker_name = target_ticker_name
        self.buyer_ticker_name = buyer_ticker_name
        self.target_ticker = Ticker(target_ticker_name)
        if self.is_buyer_company:
            self.buyer_ticker = Ticker(buyer_ticker_name)
        self.offer_price = offer_price
        self.additional_buyer_ratio = additional_buyer_ratio
        self.expecting_closing = expecting_closing
        self.commentary = commentary

    def __call__(self):
        target_history = self.target_ticker.history(period=self.period).reset_index()

        if self.is_buyer_company:
            buyer_history = self.buyer_ticker.history(period=self.period).reset_index()
            buyers_value = buyer_history.Close.values[-1]
        else:
            buyers_value = 0
            buyer_history = target_history
        final_offer_price = self.offer_price + self.additional_buyer_ratio * buyers_value
        last_date = target_history.Date.max()

        open_close_color = condition("datum.Open <= datum.Close",
                                     value("#06982d"),
                                     value("#ae1325"))

        base = Chart(target_history).encode(X("Date:T", axis=Axis(title=None)),
                                            color=open_close_color)

        rule = base.mark_rule().encode(
            Y(
                'Low:Q',
                title=f'{self.target_ticker_name}',
                scale=Scale(zero=False),
            ),
            Y2('High:Q')
        )

        bar = base.mark_bar().encode(
            Y('Open:Q'),
            Y2('Close:Q')
        )

        offer_line = base.mark_line(stroke="#F03F35", strokeDash=[1, 2]) \
            .encode(y=datum(final_offer_price))
        offer_line_text = offer_line.mark_text(color="#F03F35", dx=65, dy=7,
                                               text=f"Offer price = {final_offer_price:.1f}",
                                               fontSize=12) \
            .encode(x=value(0))

        yield_rule = base.mark_rule() \
            .transform_filter(f"year(datum.Date)=={last_date.year} && "
                              f"month(datum.Date)=={last_date.month - 1} && "
                              f"date(datum.Date)=={last_date.day}") \
            .encode(Y("Close:Q"),
                    Y2Datum(
                        datum=final_offer_price))
        yield_rule_text = yield_rule.mark_text(angle=270, baseline="bottom", dx=50, fontSize=12) \
            .transform_calculate(spread=(final_offer_price - datum.Close) / datum.Close) \
            .encode(text=Text("spread:Q", format=".2%", formatType="number"))

        dates = []
        if self.expecting_closing < last_date + timedelta(days=10):
            dates.append(self.expecting_closing)
        else:
            dates.append(last_date + timedelta(days=10))
        texts = [f"Exp. closing {self.expecting_closing.date()}"]
        e_closing_rule = Chart(DataFrame({'Date': dates,
                                          'text': texts})).mark_rule(stroke="#F03F35", strokeDash=[1, 5]) \
            .encode(x="Date:T")
        e_closing_rule_text = e_closing_rule.mark_text(stroke="#F03F35", angle=270, baseline="bottom") \
            .encode(text="text:N")

        buyer_line = Chart(buyer_history).mark_line(stroke="#BEA1A5", strokeDash=[1, 5]) \
            .encode(X("Date:T", axis=Axis(title=None)),
                    Y(
                        'Close:Q',
                        title=f'{self.buyer_ticker_name}',
                        scale=Scale(zero=False),
                    )
                    )
        chart = layer(buyer_line,
                      rule + bar + offer_line + offer_line_text + yield_rule +
                      yield_rule_text + e_closing_rule + e_closing_rule_text) \
            .resolve_scale(y="independent")
        return chart
