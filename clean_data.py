import pandas as pd
import matplotlib.pyplot as plt
import os

# python script to clean the raw_tte_stock.csv
def clean_data(input_path , output_path):
    print(f"Loading raw data from {input_path}...")

    # loading the data
    df = pd.read_csv(input_path)

    # converting data column to standard datetime objects
    df['Date'] = pd.to_datetime(df['Date'])

    #Sort chronologically (crucial for time_series)
    df = df.sort_values('Date').reset_index(drop=True)

    #check for any NaN/Null values
    null_counts = df.isnull().sum().sum()
    print(f" Found {null_counts} missing values in the dataset.")

    if null_counts > 0:
        #Used forward fill to carry the last known price across any weekend/holiday gaps
        df = df.ffill()
        print("For the missing values have been handled using forward fill (ffill).")

    duplicate_count = df.duplicated().sum()
    print(f" Found {duplicate_count} duplicate rows in the dataset.")
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"Found and removed {duplicate_count} duplicate rows.")
        print(df.columns)

    #now to save the clean dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned data successfully saved to {output_path}. ")
    print("\nSample of clean data:")
    print(df.head())
    print(df.describe())
    plt.figure(figsize = (10,5))
    plt.scatter(df["Date"],df["Volume"])
    plt.title("Volume over time")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.show()
if __name__ == "__main__":
    # collecting the raw dataset from the data folder
    RAW_PATH = os.path.join("data", "raw_tte_stock.csv")
    # creating the clean dataset and added to the data folder
    CLEAN_PATH = os.path.join("data", "clean_tte_stock.csv")

    clean_data(RAW_PATH, CLEAN_PATH)