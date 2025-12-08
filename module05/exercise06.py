import json
import time

import requests


def get_ticker_price(symbol: str):
    ticker = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}").content;
    return json.loads(ticker)

with open("resources/symbols.json", "rt") as file:
    symbols = json.load(file)
    start = time.perf_counter()
    for symbol in symbols[:50]:
        ticker = get_ticker_price(symbol)
        print(f"{symbol}: {ticker['price']}")
    elapsed_time = time.perf_counter() -start
    print(f"Elapsed time: {elapsed_time:.2f} seconds")