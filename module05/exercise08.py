import json
import time

import grequests


def get_async_tickers(symbols: str) -> dict[str,str]:
    return (grequests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}") for symbol in symbols);

with open("resources/symbols.json", "rt") as file:
    symbols = json.load(file)
    start = time.perf_counter()
    for response in grequests.map(get_async_tickers(symbols[:50])):
        print(response.content)
    elapsed_time = time.perf_counter() - start
    print(f"elapsed time: {elapsed_time:3.2f}")