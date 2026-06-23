import os
import pandas as pd


def engineer_features(input_path, asi_path, output_path):
    print(f"Loading the clean data from {input_path}...")
    df = pd.read_csv(input_path)

    print(f"Loading the macroeconomic data from {asi_path}...")
    asi_df = pd.read_csv(asi_path)

    # Ensuring that the date is sorted properly for the main stock
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values('Date').reset_index(drop=True)

    # Process the ASI market index data
    asi_df["Date"] = pd.to_datetime(asi_df["Date"])
    asi_df = asi_df.sort_values('Date').reset_index(drop=True)

    # Calculate the Macro Daily Return for the entire market
    asi_df['ASI_Daily_Return'] = asi_df['Close'].pct_change()

    # Merge the macro data into the main TotalEnergies dataframe
    print("Merging macroeconomic indicators...")
    df = pd.merge(df, asi_df[['Date', 'ASI_Daily_Return']], on='Date', how='left')

    print("Engineering mathematical features...")

    # Trend Features: Moving Averages(Short-term vs Mid-term)
    df['SMA_7'] = df['Close'].rolling(window=7).mean()
    df['SMA_21'] = df['Close'].rolling(window=21).mean()

    # Momentum Features: Daily Returns(Percentage change)
    df['Daily_Return'] = df['Close'].pct_change()

    # History Features: Lags (Giving the model a memory of the past 3 days)
    df['Close_Lag_1'] = df['Close'].shift(1)
    df['Close_Lag_2'] = df['Close'].shift(2)
    df['Close_Lag_3'] = df['Close'].shift(3)

    # Target Variable: what we actually want to predict (Next Day's Close)
    df['Target_Next_Close'] = df['Close'].shift(-1)

    # Because we used windows and shifts, the first 21 rows will have missing values (NaN)
    # and the absolute last row won't have a target next-day price. let's drop them.
    df_cleaned = df.dropna().copy()

    # Save our newly enriched dataset
    df_cleaned.to_csv(output_path, index=False)
    print(f"✅ Success! Engineered features saved to {output_path}")
    print(f"Dataset shape went from {df.shape} to {df_cleaned.shape} after dropping boundary rows")

    # I updated your print preview to show the new macro feature!
    print("\nSample of your new features (first 3 rows):")
    print(df_cleaned[['Date', 'Close', 'SMA_7', 'ASI_Daily_Return', 'Target_Next_Close']].head(3))


if __name__ == "__main__":
    CLEAN_PATH = os.path.join("data", "clean_tte_stock.csv")
    ASI_PATH = os.path.join("data", "asi_raw.csv")  # The macro data we just fetched
    FEATURES_PATH = os.path.join("data", "features_tte_stock.csv")

    engineer_features(CLEAN_PATH, ASI_PATH, FEATURES_PATH)