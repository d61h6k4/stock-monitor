from altair import Chart
from dataclasses import dataclass
from datetime import datetime, timedelta
from pandas import DataFrame
from pathlib import Path
from yfinance import Ticker

from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    """ """


session = CachedLimiterSession(
    per_second=0.9,
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache(str(Path(__file__).parent.parent.resolve() / "yfinance.cache")),
)


@dataclass(frozen=True)
class Expectation:
    price: float
    date: datetime


@dataclass
class Stock:
    ticker_name: str
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    period: str
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    interval: str = "1d"
    # propagated data
    history: DataFrame | None = None
    # optional data
    buy_date: datetime | None = None
    last_date: datetime | None = None
    expectation: Expectation | None = None
    # mutable data
    title: str = ""
    price_chart: Chart | None = None
    volume_chart: Chart | None = None
    description: str = ""

    def __post_init__(self):
        valid_periods = {"1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"}
        if self.period not in valid_periods:
            raise ValueError(f"Given period {self.period} is not valid. Valid periods: {','.join(valid_periods)}")
        valid_intervals = set("1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo".split(","))
        if self.interval not in valid_intervals:
            raise ValueError(
                f"Given interval {self.interval} is not valid. Valid intervals: {','.join(valid_intervals)}")

        ticker = Ticker(self.ticker_name, session=session)
        self.history = ticker.history(period=self.period, interval=self.interval)

        self.last_date = self.history.reset_index().Date.max()
        # when buy date is today but we don't have data for today yet.
        if self.buy_date is not None:
            assert isinstance(self.last_date, datetime), (self.ticker_name, self.history.Date)
            if self.last_date < self.buy_date:
                self.buy_date = None


@dataclass
class Arbitrage:
    target: Stock
    buyer: Stock | str
    offer_price: float
    additional_buyer_ratio: float
    expecting_closing: datetime
    commentary: str
