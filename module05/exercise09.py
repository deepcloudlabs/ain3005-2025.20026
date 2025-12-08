import json
import time
from concurrent.futures import ThreadPoolExecutor

import requests

def get_ticker(symbol: str) -> dict:
    return requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")

from asyncio import Future


def get_all_tickers(symbols: list[str]) -> list[str]:
    ticker_futures: list[Future] = []
    tickers: list[str] = []
    with ThreadPoolExecutor(max_workers=1024) as tpe:
        for symbol in symbols:
            ticker_futures.append(tpe.submit(get_ticker, symbol))
        for ticker_future in ticker_futures:
            tickers.append(str(ticker_future.result().content))
    return tickers

with open("resources/symbols.json", "rt") as file:
    symbols = json.load(file)
    start = time.perf_counter()
    for ticker in get_all_tickers(symbols[:]):
        print(ticker)
    elapsed_time = time.perf_counter() - start
    print(f"elapsed time: {elapsed_time:3.2f}")