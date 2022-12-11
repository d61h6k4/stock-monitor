from altair import Axis, Chart, Scale, X, Y, layer, Tooltip, value, datum, condition, Y2
from datetime import datetime, timedelta, timezone
from pandas import DataFrame
from yfinance import Ticker
from typing import NamedTuple, Optional


class StockChart(NamedTuple):
    title: str
    chart: Chart
    description: str


class Stock:
    def __init__(self, ticker_name: str, period: str = "6mo", buy_date: Optional[datetime] = None):
        self.ticker_name = ticker_name
        self.period = period
        self.ticker = Ticker(self.ticker_name)
        self.history = self.ticker.history(period=self.period).reset_index()

        # when buy date is today but we don't have data for today yet.
        if buy_date is not None:
            last_date = self.history.Date.max()
            if last_date < buy_date:
                buy_date = None

        self.buy_date = buy_date

    def base_strategy(self) -> Optional[StockChart]:

        description = ""
        loss_th = 0.08

        open_close_color = condition("datum.Open <= datum.Close",
                                     value("#06982d"),
                                     value("#ae1325"))

        base = Chart(self.history).encode(X("Date:T", axis=Axis(title=None)),
                                          color=open_close_color)

        rule = base.mark_rule().encode(
            Y(
                'Low:Q',
                title=f'{self.ticker_name}',
                scale=Scale(zero=False)
            ),
            Y2('High:Q')
        )

        bar = base.mark_bar().encode(
            Y('Open:Q'),
            Y2('Close:Q')
        )
        t_line = rule + bar

        t_ma_line = base.mark_line(stroke="#FF8788", strokeDash=[1, 5]) \
            .transform_window(ma10="mean(Close)",
                              frame=[-10, 0]) \
            .encode(y="ma10:Q",
                    tooltip=[Tooltip("ma10:Q", title="Moving average 10 days")])
        if self.buy_date is None:
            return StockChart(title=f"{self.ticker_name}", chart=t_line + t_ma_line, description=description)

        description = "\n\nSell when the stock price crosses `cut the loss` line."
        buy_price = self.history.iloc[self.history.Date.searchsorted(self.buy_date)]["Open"]

        cut_loss = base.mark_line(stroke="#F03F35", strokeDash=[1, 2]).encode(y=datum(buy_price * (1 - loss_th)))
        cut_loss_text = cut_loss.mark_text(color="#F03F35", dx=60, dy=7,
                                           text=f"cut the loss (-{100 * loss_th:.0f}% of buy price)",
                                           fontSize=8) \
            .encode(x=value(0))
        cut_loss_intersection = base.mark_point(color="#F03F35") \
            .encode(y="Close") \
            .transform_filter(f"year(datum.Date)>={self.buy_date.year} && "
                              f"month(datum.Date)>={self.buy_date.month - 1} && "
                              f"date(datum.Date)>={self.buy_date.day}") \
            .transform_filter(datum.Close < buy_price * (1 - loss_th))
        take_gain = base.mark_line(stroke="#32B67A", strokeDash=[1, 5]) \
            .encode(y=datum(buy_price * (1 + 0.25)))
        take_gain_text = take_gain.mark_text(color="#32B67A", dx=70, dy=-7, text="take the gain (+25% of buy price)",
                                             fontSize=8) \
            .encode(x=value(0))
        take_gain_intersection = base.mark_point(color="#32B67A") \
            .encode(y="Close") \
            .transform_filter(f"year(datum.Date)>={self.buy_date.year} && "
                              f"month(datum.Date)>={self.buy_date.month - 1} && "
                              f"date(datum.Date)>={self.buy_date.day}") \
            .transform_filter(datum.Close > buy_price * (1 + 0.25))

        dates = [self.buy_date]
        texts = ["bought"]
        if self.buy_date + timedelta(weeks=3) < datetime.now(tz=timezone.utc):
            dates.append(self.buy_date + timedelta(weeks=3))
            texts.append('too early')
        if self.buy_date + timedelta(weeks=8) < datetime.now(tz=timezone.utc):
            dates.append(self.buy_date + timedelta(weeks=8))
            texts.append('reevaluate')

        rules = Chart(DataFrame({'Date': dates,
                                 'text': texts})).mark_rule(strokeDash=[1, 5]).encode(x="Date:T")
        rules_text = rules.mark_text(angle=270, baseline="bottom").encode(text="text:N")

        chart = t_line + t_ma_line + cut_loss + cut_loss_text + cut_loss_intersection + take_gain + take_gain_text + \
                take_gain_intersection + rules + rules_text
        return StockChart(title=f"{self.ticker_name}", chart=chart, description=description)

    def vix_strategy(self) -> StockChart:
        description = "When ^VIX crosses `sell` line, sell the stock, when ^VIX crosses `buy` line, buy the stock." \
                      "\n\nMoving average 10 days - short term price trend."

        vix_history = Ticker("^VIX").history(period=self.period)
        vix_history["buy"] = 30
        vix_history["sell"] = 20
        source = self.history.join(vix_history, on="Date", rsuffix="_vix").reset_index()
        base = Chart(source).encode(
            X("Date:T", axis=Axis(title=None))
        )

        base_strategy = self.base_strategy()
        description += base_strategy.description
        t_chart = base_strategy.chart

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
        return StockChart(title="^VIX strategy", chart=chart, description=description)
