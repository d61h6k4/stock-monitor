import requests
import json

from tqdm import tqdm
from stock_monitor.models import Stock
from stock_monitor.data import ideas, stocks

_BOT_URL = "https://lochaufwallstrasse.de/bot/conversations/dbihbka/trigger_intent?output_channel=callback"


def watch(stock):
    r = requests.post(_BOT_URL, data=json.dumps({"name": "ask_set_watchlist_reminder",
                                                 "entities": {
                                                     "ticker": stock.ticker_name,
                                                     "seconds": 43200
                                                 }}))
    r.raise_for_status()


def unwatch(stock):
    r = requests.post(_BOT_URL, data=json.dumps({"name": "ask_set_unwatchlist_reminder",
                                                 "entities": {
                                                     "ticker": stock.ticker_name,
                                                     "seconds": 43200
                                                 }}))
    r.raise_for_status()


def monitor(stock):
    r = requests.post(_BOT_URL, data=json.dumps({"name": "ask_set_asr_reminder",
                                                 "entities": {
                                                     "ticker": stock.ticker_name,
                                                     "seconds": 3600
                                                 }}))

    r.raise_for_status()


def main():
    for idea in tqdm(ideas(period="3mo", interval="1d"), desc="Processing ideas..."):
        watch(idea)

    for stock in tqdm(stocks(period="3mo", interval="1d"), desc="Processing portfolio..."):
        monitor(stock)


if __name__ == "__main__":
    main()
