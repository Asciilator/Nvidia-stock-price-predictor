import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import yfinance as yf

# Step 1: Load Nvidia Stock Data
def load_data(ticker="NVDA", start_date="2022-01-01", end_date="2023-01-01"):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data['Date'] = stock_data.index
    return stock_data

# Step 2: Moving Average Model
def moving_average_prediction(data, window=5):
    data['Moving_Avg'] = data['Close'].rolling(window=window).mean()
    return data

# Step 3: Linear Regression Model
def linear_regression_prediction(data):
    # Prepare the data
    data['Days'] = np.arange(len(data))  # Use the number of days as a feature
    X = data[['Days']]
    y = data['Close']
    
    # Split into training and test set (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict on test set
    y_pred = model.predict(X_test)

    # Evaluate performance using Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    print(f"Linear Regression Mean Squared Error: {mse}")

    # Add predictions to the data frame
    data['Linear_Regression_Pred'] = np.nan
    data.loc[X_test.index, 'Linear_Regression_Pred'] = y_pred

    return data

# Step 4: Visualize the Predictions
def visualize_predictions(data):
    plt.figure(figsize=(14, 7))
    
    # Plot actual prices
    plt.plot(data['Date'], data['Close'], label="Actual Prices", color='blue')

    # Plot moving average predictions
    plt.plot(data['Date'], data['Moving_Avg'], label=f"Moving Average (window=5)", color='green')

    # Plot linear regression predictions
    plt.plot(data['Date'], data['Linear_Regression_Pred'], label="Linear Regression Prediction", color='red')

    plt.title("Nvidia Stock Price Prediction")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 5: Main function to run everything
def main():
    # Load data
    stock_data = load_data()

    # Moving average prediction
    stock_data = moving_average_prediction(stock_data)

    # Linear regression prediction
    stock_data = linear_regression_prediction(stock_data)

    # Visualize the predictions
    visualize_predictions(stock_data)

if __name__ == "__main__":
    main()

