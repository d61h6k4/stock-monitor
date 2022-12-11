from altair import Chart
from dataclasses import dataclass
from datetime import datetime, timedelta
from pandas import DataFrame
from yfinance import Ticker


@dataclass
class Stock:
    ticker_name: str
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    period: str
    # propagated data
    history: DataFrame | None = None
    # optional data
    buy_date: datetime | None = None
    # mutable data
    title: str = ""
    price_chart: Chart | None = None
    volume_chart: Chart | None = None
    description: str = ""

    def __post_init__(self):
        valid_periods = {"1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"}
        if self.period not in valid_periods:
            raise ValueError(f"Given period {self.period} is not valid. Valid periods: {','.join(valid_periods)}")

        ticker = Ticker(self.ticker_name)
        self.history = ticker.history(period=self.period).reset_index()

        # when buy date is today but we don't have data for today yet.
        if self.buy_date is not None:
            last_date = self.history.Date.max()
            if last_date < self.buy_date:
                self.buy_date = None


@dataclass
class Arbitrage:
    target: Stock
    buyer: Stock | str
    offer_price: float
    additional_buyer_ratio: float
    expecting_closing: datetime
    commentary: str

