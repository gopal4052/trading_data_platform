import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(symbol):
    """
    Fetch last 5 days of stock data for a given symbol
    """
    stock = yf.Ticker(symbol)
    df = stock.history(period="5d")
    df["symbol"] = symbol
    df["ingestion_time"] = datetime.utcnow()
    return df


if __name__ == "__main__":
    symbols = ["RELIANCE.NS", "TCS.NS"]

    for symbol in symbols:
        data = fetch_stock_data(symbol)
        print(f"\nData for {symbol}:")
        print(data.head())
