import pandas as pd
import yfinance as yf


def moving_average_strategy(ticker="AAPL", short_window=50, long_window=200):
    """Fetch historical data and compute a simple moving average crossover."""
    data = yf.download(ticker, period="1y", interval="1d")
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker}")

    data["ma_short"] = data["Adj Close"].rolling(window=short_window).mean()
    data["ma_long"] = data["Adj Close"].rolling(window=long_window).mean()

    data["signal"] = 0
    data.loc[data["ma_short"] > data["ma_long"], "signal"] = 1
    data["position"] = data["signal"].diff().fillna(0)
    return data


if __name__ == "__main__":
    df = moving_average_strategy()
    print(df.tail())
