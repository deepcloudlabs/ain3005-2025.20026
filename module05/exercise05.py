import json
import requests

response = requests.get("https://api.binance.com/api/v3/ticker/price").content;
tickers = json.loads(response)

with open("resources/symbols.json", "wt") as file:
    symbols = []
    for ticker in tickers:
        symbols.append(ticker["symbol"])
    json.dump(symbols, file)