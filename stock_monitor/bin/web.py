from altair import vconcat
from streamlit import altair_chart, tabs, write, caption, sidebar, selectbox, set_page_config, markdown, title, form, \
    number_input, select_slider, form_submit_button
from stock_monitor.models import Stock, Arbitrage
from stock_monitor.renders.stock import base_strategy, vix_strategy
from stock_monitor.renders.arbitrages import arbitrage_strategy
from stock_monitor.data import tickers, arbitrages, stocks


def render_position_size():
    with form("position_size_calculator", clear_on_submit=True):
        write("Position size calculator")
        portfolio_size = number_input("Account size (in $):", min_value=0)
        risk_ratio = select_slider("Risk ratio (in %):", value=2, options=range(1, 9))
        submitted = form_submit_button("Calculate")
        if submitted:
            position_size = portfolio_size * (0.01 * risk_ratio) / 0.08
            msg = f"""When buying **${position_size:,.2f}** worth of stock and following the loss reduction rule
                      (selling a stake when its value is lost by 8% of its purchase price),
                      your losses will not exceed **{risk_ratio}%** of the size of your portfolio.
                   """
            markdown(msg)


def render_sentiment():
    write("Sentiment figures are going to be here")


def render_arbitrage(a: Arbitrage):
    a.target = base_strategy(a.target)
    if isinstance(a.buyer, str):
        buyer_ticker_name = a.buyer
    else:
        buyer_ticker_name = a.buyer.ticker_name
        a.buyer = base_strategy(a.buyer)

    title(f"{buyer_ticker_name} buys {a.target.ticker_name}")
    altair_chart(arbitrage_strategy(a), use_container_width=True)
    markdown(a.commentary)


def render_ticker(stock: Stock):
    stock = base_strategy(stock)
    if stock.ticker_name in {"GOOG", "NVDA", "ASML", "KLAC"}:
        stock = vix_strategy(stock)

    title(stock.title)
    altair_chart(vconcat(stock.price_chart.properties(width=1192),
                         stock.volume_chart.properties(height=50, width=1192)),
                 use_container_width=True)
    caption(stock.description)


set_page_config(layout="wide", initial_sidebar_state="collapsed")
title(u":orange[L]och :orange[A]uf :orange[W]allstra&szlig;e")

with sidebar:
    PERIOD = selectbox("Period", ("3mo", "6mo", "1y", "2y", "5y", "max"))
assert PERIOD is not None

tabs_name = ["Position size", "Arbitrage"] + tickers()

for tab_name, tab in zip(tabs_name, tabs(tabs_name)):
    match tab_name:
        case "Position size":
            with tab:
                render_position_size()
        case "Sentiment":
            with tab:
                render_sentiment()
        case "Arbitrage":
            with tab:
                for arbitrage in arbitrages(PERIOD):
                    render_arbitrage(arbitrage)
        case _:
            with tab:
                for s in stocks(PERIOD):
                    if s.ticker_name == tab_name:
                        render_ticker(s)
