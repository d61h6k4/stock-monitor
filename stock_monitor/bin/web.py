from altair import vconcat
from pandas import DataFrame
from streamlit import altair_chart, tabs, write, caption, sidebar, selectbox, set_page_config, markdown, title, form, \
    number_input, select_slider, form_submit_button, subheader, text_input
from stock_monitor.models import Stock, Arbitrage
from stock_monitor.renders.stock import base_strategy, vix_strategy, idea_strategy, mad_strategy, atr_strategy
from stock_monitor.renders.arbitrages import arbitrage_strategy
from stock_monitor.data import arbitrages, stocks, vix_stocks, tax_loss_jan_stocks, ideas


def render_position_size():
    with form("position_size_calculator", clear_on_submit=False):
        write("Position size calculator")
        ticker_name = text_input("Ticker:")
        portfolio_size = number_input("Account size (in $):", min_value=0)
        risk_ratio = select_slider("Risk ratio (in %):", value=2, options=range(1, 9))
        submitted = form_submit_button("Calculate")
        if submitted:
            s = Stock(ticker_name, period="1y", interval="1d")

            df = s.history
            # https://raposa.trade/blog/atr-and-how-top-traders-size-their-positions/
            atr = (DataFrame([df["High"] - df["Low"],
                              (df["High"] - df["Close"].shift(1)).fillna(0.0),
                              (df["Close"].shift(1) - df["Low"]).fillna(0.0)])
                   .T.max(axis=1).rolling(5).mean().last(offset='1d'))
            price = df["Close"].last(offset='1d').values[0]
            atr_shares_num = int(risk_ratio * float(portfolio_size) / (2. * atr * price))
            atr_position_size = atr_shares_num * price
            position_size = portfolio_size * (0.01 * risk_ratio) / 0.08
            msg = f"""When buying **${position_size:,.2f}** worth of stock and following the loss reduction rule
                      (selling a stake when its value is lost by 8% of its purchase price),
                      your losses will not exceed **{risk_ratio}%** of the size of your portfolio.
                   """
            markdown(msg)
            markdown(f"Another strategy based on ATR: buy **{atr_shares_num}** shares which cost today **${atr_position_size:,.2f}**")
            render_ticker(Stock(ticker_name, period="3mo", interval="1d", buy_date=s.last_date))


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
    altair_chart(arbitrage_strategy(a), use_container_width=True, theme="streamlit")
    markdown(a.commentary)


def render_vix_strategy(stock: Stock):
    if stock.price_chart is None:
        stock = vix_strategy(base_strategy(stock))
    title(stock.title)
    altair_chart(vconcat(stock.price_chart.properties(width=1192),
                         stock.volume_chart.properties(height=50, width=1192)),
                 use_container_width=True, theme="streamlit")
    caption(stock.description)


def render_ticker(stock: Stock):
    if stock.price_chart is None:
        stock = mad_strategy(atr_strategy(stock))

    title(stock.title)
    altair_chart(vconcat(stock.price_chart.properties(width=1192),
                         stock.volume_chart.properties(height=50, width=1192)),
                 use_container_width=True, theme="streamlit")
    markdown(stock.description)


def render_idea(stock: Stock):
    if stock.price_chart is None:
        stock = idea_strategy(base_strategy(stock))

    title(stock.title)
    altair_chart(vconcat(stock.price_chart.properties(width=1192),
                         stock.volume_chart.properties(height=50, width=1192)),
                 use_container_width=True, theme="streamlit")
    markdown(stock.description)


set_page_config(page_title="lawallstra&szlig;e", page_icon=":chart:", layout="wide",
                initial_sidebar_state="collapsed")
title(u":orange[L]och :orange[A]uf :orange[W]allstra&szlig;e")

with sidebar:
    PERIOD = selectbox("Period", ("3mo", "6mo", "1y", "2y", "5y", "max"))
    INTERVAL = selectbox("Inetrval", ("1d", "1wk"))
assert PERIOD is not None
assert INTERVAL is not None

tabs_name = ["Position size", "Arbitrage", "VIX", "Portfolio", "Ideas"]

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
        case "VIX":
            with tab:
                subheader("^VIX strategy")
                for stock in vix_stocks(PERIOD, INTERVAL):
                    render_vix_strategy(stock)
        case "January Effect":
            with tab:
                subheader("TAX LOSS \"JANUARY EFFECT\" (SMALL CAP) STOCK IDEAS")
                caption("2022 has been a bear, with many stocks down -80%, -90%, -95% or more. \
                       At YE, holders are often eager to lock-in tax losses & clean-up their books. \
                       So we could see some nice bounces once the selling abates.")
                markdown("[source.](https://twitter.com/RagingVentures/status/1604244196273143808)")
                for stock in tax_loss_jan_stocks(PERIOD, INTERVAL):
                    render_ticker(stock)
        case "Portfolio":
            with tab:
                for s in stocks(PERIOD, INTERVAL):
                    render_ticker(s)
        case "Ideas":
            with tab:
                for s in ideas(PERIOD, INTERVAL):
                    render_idea(s)
