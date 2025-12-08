import asyncio
import json
import time

import requests


async def get_ticker_price(symbol: str) -> dict[str,str]:
    ticker = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}").content;
    #print(f"get_ticker_price() sending the request to the server...{symbol}")
    return json.loads(ticker)
async def app():
    with open("resources/symbols.json", "rt") as file:
        symbols = json.load(file)
        start = time.perf_counter()
        tickers = []
        for symbol in symbols[:50]:
            ticker = get_ticker_price(symbol)
            print(f"sending the request to the server...{symbol}")
            tickers.append(ticker)
        all_tickers = await asyncio.gather(*tickers)
        elapsed_time = time.perf_counter() -start
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        for ticker in all_tickers:
            print(f"{ticker['symbol']}: {ticker['price']}")

asyncio.run(app())