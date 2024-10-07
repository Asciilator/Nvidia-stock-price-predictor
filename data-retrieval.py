import yfinance as yf
import pandas as pd

# Step 1: Define the function to retrieve stock data and save as CSV
def retrieve_and_save_stock_data(ticker="NVDA", start_date="2022-01-01", end_date="2023-01-01", filename="nvidia_stock_data.csv"):
    """
    Retrieve stock data for a given ticker and date range, and save it to a CSV file. 

    Args:
        ticker (str, optional): The stock ticker symbol to retrieve data for. Defaults to "NVDA".
        start_date (str, optional): The start date for the data in "YYYY-MM-DD" format. Defaults to "2022-01-01".
        end_date (str, optional): The end date for the data in "YYYY-MM-DD" format. Defaults to "2023-01-01".
        filename (str, optional): The name of the CSV file to save the data to. Defaults to "nvidia_stock_data.csv".

    Returns:
        None: This function does not return any values. It saves the stock data to a CSV file.
    """
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