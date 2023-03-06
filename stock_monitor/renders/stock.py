from altair import Axis, Chart, Scale, X, Y, layer, Tooltip, value, datum, condition, Y2, Y2Datum, Text
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pandas import DataFrame
from stock_monitor.models import Stock


def base_strategy(stock: Stock) -> Stock:
    loss_th = 0.08

    open_close_color = condition("datum.Open <= datum.Close",
                                 value("#06982d"),
                                 value("#ae1325"))

    base = Chart(stock.history.reset_index()).encode(X("Date:T", axis=Axis(title=None)),
                                                     color=open_close_color)

    rule = base.mark_rule().encode(
        Y(
            'Low:Q',
            title=f'{stock.ticker_name}',
            scale=Scale(zero=False)
        ),
        Y2('High:Q')
    )

    bar = base.mark_bar().encode(
        Y('Open:Q'),
        Y2('Close:Q')
    )
    t_line = rule + bar

    stock.volume_chart = base.mark_bar().encode(Y('Volume:Q'))
    if stock.buy_date is None:
        stock.title = f"{stock.ticker_name}"
        stock.price_chart = t_line
        return stock

    description = "\n\nSell when the stock price crosses `cut the loss` line."
    buy_price = stock.history.iloc[stock.history.Date.searchsorted(stock.buy_date)]["Open"]

    cut_loss = base.mark_line(stroke="#F03F35", strokeDash=[1, 2]).encode(y=datum(buy_price * (1 - loss_th)))
    cut_loss_text = cut_loss.mark_text(color="#F03F35", dx=60, dy=7,
                                       text=f"cut the loss (-{100 * loss_th:.0f}% of buy price)",
                                       fontSize=8) \
        .encode(x=value(0))
    filter_buy_date = f"year(datum.Date)>={stock.buy_date.year} && " \
                      f"month(datum.Date)>={stock.buy_date.month - 1} && " \
                      f"date(datum.Date)>={stock.buy_date.day}"
    cut_loss_intersection = base.mark_point(color="#F03F35") \
        .encode(y="Close") \
        .transform_filter(filter_buy_date) \
        .transform_filter(datum.Close < buy_price * (1 - loss_th))
    take_gain = base.mark_line(stroke="#32B67A", strokeDash=[1, 5]) \
        .encode(y=datum(buy_price * (1 + 0.25)))
    take_gain_text = take_gain.mark_text(color="#32B67A", dx=70, dy=-7, text="take the gain (+25% of buy price)",
                                         fontSize=8) \
        .encode(x=value(0))
    take_gain_intersection = base.mark_point(color="#32B67A") \
        .encode(y="Close") \
        .transform_filter(filter_buy_date) \
        .transform_filter(datum.Close > buy_price * (1 + 0.25))

    dates = [stock.buy_date]
    texts = ["bought"]
    if stock.buy_date + timedelta(weeks=3) < datetime.now(tz=timezone.utc):
        dates.append(stock.buy_date + timedelta(weeks=3))
        texts.append('too early')
    elif stock.buy_date + timedelta(weeks=8) < datetime.now(tz=timezone.utc):
        dates.append(stock.buy_date + timedelta(weeks=8))
        texts.append('reevaluate')

    rules = Chart(DataFrame({'Date': dates,
                             'text': texts})).mark_rule(color="#ABCEE2", strokeDash=[1, 5]).encode(x="Date:T")
    rules_text = rules.mark_text(color="#ABCEE2", angle=270, baseline="bottom").encode(text="text:N")

    chart = t_line + cut_loss + cut_loss_text + cut_loss_intersection + take_gain + take_gain_text + \
            take_gain_intersection + rules + rules_text

    stock.title = f"{stock.ticker_name}"
    stock.price_chart = chart
    stock.description += description

    return stock


def atr_strategy(stock: Stock) -> Stock:
    open_close_color = condition("datum.Open <= datum.Close",
                                 value("#06982d"),
                                 value("#ae1325"))

    base = Chart(stock.history.reset_index()).encode(X("Date:T", axis=Axis(title=None)),
                                                     color=open_close_color)

    rule = base.mark_rule().encode(
        Y(
            'Low:Q',
            title=f'{stock.ticker_name}',
            scale=Scale(zero=False)
        ),
        Y2('High:Q')
    )

    bar = base.mark_bar().encode(
        Y('Open:Q'),
        Y2('Close:Q')
    )
    t_line = rule + bar

    stock.volume_chart = base.mark_bar().encode(Y('Volume:Q'))

    df = Stock(stock.ticker_name, period="1y", interval="1d").history

    if stock.buy_date is not None:
        buy_price = df.loc[stock.buy_date.date().isoformat()]["Open"]
    else:
        buy_price = 0
        
    # https://raposa.trade/blog/atr-and-how-top-traders-size-their-positions/
    atr = (DataFrame([df["High"] - df["Low"],
                      (df["High"] - df["Close"].shift(1)).fillna(0.0),
                      (df["Close"].shift(1) - df["Low"]).fillna(0.0)])
           .T.max(axis=1).rolling(5).mean().last(offset='1d'))
    price = df["Close"].last(offset='1d')
    sell_price = (price - 2 * atr).values[0]
    cut_loss = base.mark_line(stroke="#F03F35", strokeDash=[1, 2]).encode(y=datum(sell_price))
    cut_loss_text = cut_loss.mark_text(color="#F03F35", dx=30, dy=7,
                                       text=f"sell on {sell_price:,.2f}",
                                       fontSize=12) \
        .encode(x=value(0))

    cut_loss_eight_prt = base.mark_line(stroke="#F03F35", strokeDash=[1, 5]) \
        .encode(y=datum(buy_price * (1.0 - 0.08)))
    cut_loss_eight_prt_text = cut_loss_eight_prt.mark_text(color="#F03F35", dx=70, dy=-7,
                                                           text=f"sell on {buy_price * (1.0 - 0.08):,.2f} (-8%)",
                                                           fontSize=8) \
        .encode(x=value(0))
    take_gain = base.mark_line(stroke="#32B67A", strokeDash=[1, 5]) \
        .encode(y=datum(buy_price * (1 + 0.25)))
    take_gain_text = take_gain.mark_text(color="#32B67A", dx=70, dy=-7, text="take the gain (+25% of buy price)",
                                         fontSize=8) \
        .encode(x=value(0))
    dates = [stock.buy_date]
    texts = ["bought"]
    if stock.buy_date + timedelta(weeks=3) < datetime.now(tz=timezone.utc):
        dates.append(stock.buy_date + timedelta(weeks=3))
        texts.append('too early')
    if stock.buy_date + timedelta(weeks=8) < datetime.now(tz=timezone.utc):
        dates.append(stock.buy_date + timedelta(weeks=8))
        texts.append('reevaluate')

    rules = Chart(DataFrame({'Date': dates,
                             'text': texts})).mark_rule(color="#ABCEE2", strokeDash=[1, 5]).encode(x="Date:T")
    rules_text = rules.mark_text(color="#ABCEE2", angle=270, baseline="bottom").encode(text="text:N")

    chart = t_line + cut_loss + cut_loss_text + rules + rules_text + take_gain + \
            take_gain_text + cut_loss_eight_prt + cut_loss_eight_prt_text

    stock.title = f"{stock.ticker_name}"
    stock.price_chart = chart

    return stock


def mad_strategy(stock: Stock) -> Stock:
    assert stock.price_chart is not None, "MAD strategy appliable only to the already evaluated strategy"
    t_chart = stock.price_chart

    data = Stock(stock.ticker_name, period="1y", interval="1d").history
    data.drop(["Open", "Low", "High", "Volume", "Dividends", "Stock Splits"], axis=1, inplace=True)

    mad_data = (data["Close"].rolling(21).mean() / data["Close"].rolling(50).mean()).fillna(1.0).reset_index().rename(
        columns={"Close": "MAD"})

    base = Chart(stock.history.reset_index().merge(mad_data, on="Date", how="left")).encode(
        X("Date:T", axis=Axis(title=None))
    )
    mad_line = base.mark_line(stroke="#61BFAD", strokeDash=[3, 5]) \
        .encode(y=Y("MAD",
                    scale=Scale(zero=False)), tooltip=[Tooltip("MAD", title="Moving average distance 21/50")])

    buy_line = base.mark_line(stroke="#32B67A", strokeDash=[1, 2]).encode(y=datum(1.0))
    buy_line_text = buy_line.mark_text(color="#32B67A", dx=30, dy=7,
                                       text="buy",
                                       fontSize=12) \
        .encode(x=value(0))

    chart = layer(mad_line + buy_line + buy_line_text, t_chart).resolve_scale(y="independent")

    stock.price_chart = chart
    return stock


def vix_strategy(stock: Stock) -> Stock:
    description = "When ^VIX crosses `sell` line, sell the stock, when ^VIX crosses `buy` line, buy the stock." \
                  "\n\nMoving average 10 days - short term price trend."

    vix_history = Stock("^VIX", period=stock.period).history
    vix_history["buy"] = 30
    vix_history["sell"] = 20
    source = stock.history.reset_index().join(vix_history, on="Date", rsuffix="_vix").reset_index()
    base = Chart(source).encode(
        X("Date:T", axis=Axis(title=None))
    )

    assert stock.price_chart is not None, "Vix strategy appliable only to the already evaluated strategy"
    t_chart = stock.price_chart

    vix_line = base.mark_line(stroke="#8B743D") \
        .encode(Y("Close_vix:Q",
                  axis=Axis(title="^VIX", titleColor="#8B743D"),
                  scale=Scale(zero=False)),
                tooltip=[Tooltip("Close_vix", title=f"^VIX value")]
                )
    sell_line = vix_line.mark_line(stroke="#E44A66", strokeDash=[1, 1]) \
        .encode(y="sell")
    sell_text = sell_line.mark_text(color="#E44A66", dx=10, dy=-10, text="sell", fontSize=8) \
        .encode(x=value(0))
    sell_intersection = vix_line.mark_point(color="#E44A66") \
        .encode(y="Close_vix") \
        .transform_filter(datum.Close_vix < datum.sell)

    buy_line = vix_line.mark_line(stroke="#78A15D", strokeDash=[1, 1]) \
        .encode(y="buy")
    buy_text = buy_line.mark_text(color="#78A15D", dx=10, dy=10, text="buy", fontSize=8) \
        .encode(x=value(0))
    buy_intersection = vix_line.mark_point(color="#78A15D") \
        .encode(y="Close_vix") \
        .transform_filter(datum.Close_vix > datum.buy)

    chart = layer(vix_line + sell_line + sell_text + sell_intersection + buy_line + buy_text + buy_intersection,
                  t_chart).resolve_scale(y="independent")
    stock.title = stock.ticker_name
    stock.price_chart = chart
    stock.description += description
    return stock


def idea_strategy(stock: Stock) -> Stock:
    assert stock.price_chart is not None, "Idea strategy appliable only to the already evaluated strategy"
    assert stock.expectation is not None, "Idea strategy valid only if we have expectations."

    base = Chart(stock.history.reset_index()).encode(X("Date:T", axis=Axis(title=None)))

    expectation_line = base.mark_line(color="#ABCEE2", strokeDash=[1, 2]) \
        .encode(y=datum(stock.expectation.price))
    text = f"Expectation price = {stock.expectation.price:.1f} by {stock.expectation.date.strftime('%Y-%m-%d')}"
    expectation_line_text = expectation_line.mark_text(color="#ABCEE2", dx=105, dy=7,
                                                       text=text,
                                                       fontSize=12) \
        .encode(x=value(0))

    yield_rule = base.mark_rule(color="#ABCEE2", ) \
        .transform_filter(f"year(datum.Date)=={stock.last_date.year} && "
                          f"month(datum.Date)=={stock.last_date.month - 1} && "
                          f"date(datum.Date)=={stock.last_date.day}") \
        .encode(Y("Close:Q"),
                Y2Datum(
                    datum=stock.expectation.price))

    yield_rule_text = yield_rule.mark_text(color="#ABCEE2", angle=270, baseline="bottom", dx=50, fontSize=12) \
        .transform_calculate(spread=(stock.expectation.price - datum.Close) / datum.Close) \
        .encode(text=Text("spread:Q", format=".2%", formatType="number"))

    chart = expectation_line + expectation_line_text + yield_rule + yield_rule_text
    stock.price_chart += chart
    return stock
