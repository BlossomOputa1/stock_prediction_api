import yfinance as yf
import pandas as pd
import os
import datetime


# the fetch function
def fetch_stock_data(ticker_symbol, start_date, end_date, save_path):
    print(f"Fetching data for {ticker_symbol} from {start_date} to {end_date}...")

    # Download the historical data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Check if the data was successfully downloaded
    if stock_data.empty:
        print(f"🚨 No data found for {ticker_symbol} or check your internet connection.")
        return

    # Manually flatten the columns if they are multiIndex
    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data.columns = [col[0] for col in stock_data.columns]

    # To reset the index so 'Date' becomes a standard, selectable column
    stock_data.reset_index(inplace=True)

    # Guarantee the first column is strictly named 'Date'
    stock_data.rename(columns={stock_data.columns[0]: 'Date'}, inplace=True)

    # Save the raw data (index=False prevents pandas from adding an unnecessary blank column)
    stock_data.to_csv(save_path, index=False)
    print(f"✅ Success! Data saved to {save_path}")
    print(f"Verified columns: {stock_data.columns.tolist()}\n")


if __name__ == "__main__":
    # Define the timeframe for the data
    START = "2020-01-01"
    END = datetime.date.today()

    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)

    # 1. Fetch TotalEnergies (TTE)
    TICKER_TTE = "TTE"
    FILE_PATH_TTE = os.path.join("data", "total_raw.csv")
    fetch_stock_data(TICKER_TTE, START, END, FILE_PATH_TTE)

    # 2. Fetch Nigerian Market Proxy (MSCI Nigeria ETF)
    TICKER_ASI = "NGE"
    FILE_PATH_ASI = os.path.join("data", "asi_raw.csv")
    fetch_stock_data(TICKER_ASI, START, END, FILE_PATH_ASI)