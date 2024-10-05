import yfinance as yf
import pandas as pd

# Step 1: Define the function to retrieve stock data and save as CSV
def retrieve_and_save_stock_data(ticker="NVDA", start_date="2022-01-01", end_date="2023-01-01", filename="nvidia_stock_data.csv"):
    # Download the stock data from yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Save the data to a CSV file
    stock_data.to_csv(filename)
    print(f"Data successfully saved to {filename}")

# Step 2: Call the function to retrieve and save Nvidia stock data
retrieve_and_save_stock_data(ticker="NVDA", start_date="2022-01-01", end_date="2023-01-01", filename="nvidia_stock_data.csv")

# Load the CSV file
stock_data = pd.read_csv("nvidia_stock_data.csv")

# Display the first few rows of the data
print(stock_data.head())