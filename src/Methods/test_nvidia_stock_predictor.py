import pytest
import pandas as pd
import numpy as np
from nvidia_stock_price_predictor import (
    load_data,
    moving_average_prediction,
    linear_regression_prediction
)

# Test Load Data Function
def test_load_data():
    """Test the load_data function to ensure it correctly retrieves stock data."""
    data = load_data(ticker="NVDA", start_date="2022-01-01", end_date="2022-02-01")
    
    # Ensure that data is not empty
    assert not data.empty, "Stock data should not be empty"
    
    # Ensure required columns are in the DataFrame
    assert "Close" in data.columns, "Missing 'Close' column in stock data"
    assert "Date" in data.columns, "Missing 'Date' column in stock data"
    
    # Ensure the correct number of rows based on the date range
    assert len(data) > 0, "Stock data should have rows corresponding to the date range"

# Test Moving Average Calculation
def test_moving_average_prediction():
    """Test the moving_average_prediction function to ensure correct moving average is calculated."""
    data = pd.DataFrame({
        'Close': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    })
    
    # Calculate the moving average with a window of 3
    data_with_ma = moving_average_prediction(data, window=3)
    
    # Ensure the Moving_Avg column exists
    assert 'Moving_Avg' in data_with_ma.columns, "Missing 'Moving_Avg' column"
    
    # Check that the moving average values are correct (manual verification)
    expected_ma = [np.nan, np.nan, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0]
    assert np.allclose(data_with_ma['Moving_Avg'].values, expected_ma, equal_nan=True), "Moving average values are incorrect"

# Test Linear Regression Prediction
def test_linear_regression_prediction():
    """Test the linear_regression_prediction function to ensure it makes predictions."""
    # Create sample data with a linear trend
    data = pd.DataFrame({
        'Close': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    })
    
    # Apply linear regression
    data_with_lr = linear_regression_prediction(data)
    
    # Ensure the Linear_Regression_Pred column exists
    assert 'Linear_Regression_Pred' in data_with_lr.columns, "Missing 'Linear_Regression_Pred' column"
    
    # Ensure that some predictions have been made
    assert data_with_lr['Linear_Regression_Pred'].notna().sum() > 0, "Linear regression predictions should be non-empty"
    
    # Verify the predictions follow the linear trend
    assert np.all(np.diff(data_with_lr['Linear_Regression_Pred'].dropna()) > 0), "Linear regression predictions should follow a positive trend"

