import yfinance as yf
import pandas as pd
from datetime import datetime,timezone
import os

def fetch_stock_data(symbol):
    """
    Fetch last 5 days of stock data for a given symbol
    """
    stock = yf.Ticker(symbol)
    df = stock.history(period="5d")
    df["symbol"] = symbol
    df["ingestion_time"] = datetime.now(timezone.utc)
    return df


if __name__ == "__main__":
    symbols = ["RELIANCE.NS", "TCS.NS"]

    for symbol in symbols:
        data = fetch_stock_data(symbol)
        print(f"\nData for {symbol}:")
        ingestion_date = datetime.now(timezone.utc).date().isoformat()
        bronze_path = f"/Users/gopalsharma/trading_data_platform/data/bronze/market_data/ingestion_date={ingestion_date}"
        os.makedirs(bronze_path, exist_ok=True)
        data.to_csv(f"{bronze_path}/{symbol}.csv")
        print("CSV file saved")
