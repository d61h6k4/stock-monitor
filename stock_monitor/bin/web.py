from datetime import datetime, timezone
from streamlit import altair_chart, tabs, write, title, caption, sidebar, selectbox, set_page_config
from stock_monitor.renders.stock import Stock


def tickers():
    return ["GOOG", "NVDA", "AAPL", "JNJ", "NWS"]


def render_new_stock():
    write("New stock form is going to be here")


def render_sentiment():
    write("Sentiment figures are going to be here")


def render_ticker(ticker_name: str, period: str):
    stock = Stock(ticker_name, period=period, buy_date=datetime(2022, 9, 22, tzinfo=timezone.utc)).vix_strategy()
    title(stock.title)
    altair_chart(stock.chart, use_container_width=True)
    caption(stock.description)


set_page_config(layout="wide", initial_sidebar_state="collapsed")

with sidebar:
    PERIOD = selectbox("Period", ("3mo", "6mo", "1y", "2y", "5y", "max"))
assert PERIOD is not None

tabs_name = ["New stock form", "Sentiment"] + tickers()

for tab_name, tab in zip(tabs_name, tabs(tabs_name)):
    match tab_name:
        case "New stock form":
            with tab:
                render_new_stock()
        case "Sentiment":
            with tab:
                render_sentiment()
        case _:
            with tab:
                render_ticker(tab_name, PERIOD)
