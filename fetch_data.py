import yfinance as yf
import pandas as pd
import os

# the fetch function
def fetch_stock_data(ticker_symbol, start_date, end_date, save_path):
    print(f"Fetching data for {ticker_symbol} from {start_date} to {end_date}...")

    # Download the historical data
    # TTE is the ticker for TotalEnergies
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    #Check if the data was successfully downloaded
    if stock_data.empty:
        print(f"No data found for {ticker_symbol} or check your internet connection.")
        return
    #Save the raw data to a CSV file in our data folder

    #Manually flatten the columns if they are multiIndex
    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data.columns = [col[0] for col in stock_data.columns]
    # To reset the index so 'Date' becomes a standard, selectable column
    stock_data.reset_index(inplace=True)

    #Guarantee the first column is strictly name 'Date'
    stock_data.rename(columns={stock_data.columns[0]: 'Date'}, inplace=True)
    #now to save to the raw data(index= false prevents pandas from adding an unnecessary blank column)
    stock_data.to_csv(save_path, index=False)
    print(f"Success! Date saved to {save_path}")
    print(f"Verified columns: {stock_data.columns.tolist()}")


if __name__ == "__main__":
    # Defined parameters that indicates what stocks i am working on
    TICKER = "TTE" # TOTAL ENERGIES
    START= "2020-01-01"
    END = "2026-06-01"
    FILE_PATH= os.path.join("data", "raw_tte_stock.csv")

    fetch_stock_data(TICKER, START, END, FILE_PATH)