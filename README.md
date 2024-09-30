Name: Yusuf Ascibasi
Student number: 5748011

Project description:
    The model will retrieve relevant historical data and use statistical methods to predict stock prices for unseen future inputs, and these predictions will be compared with actual outcomes to evaluate accuracy. The model for this project will predict the stock prices of the IT company Nvidia based on the demand of Graphical Processing Units (GPU's) in the previous years, market performance (i.e. S&P 500 index) and based on Nividia's past stock prices.

Algorithms: 
    Moving average: used to calculate the average of stock prices over a short window (e.g., the last 5 days). 
    Linear regression: used for past stock prices, trading volume, and demand for GPUs.

Libraries: 
    Pandas: For data manipulation and loading historical data.
    NumPy: For mathematical operations and array manipulation.
    Matplotlib: For visualizing the predicted and actual stock prices.
    Scikit-learn: For implementing linear regression.

Methods: 
    Data Preprocessing: Normalize the stock prices and GPU demand data to ensure proper scaling for the model.
    Model Evaluation: Use Mean Squared Error (MSE) or Mean Absolute Error (MAE) to evaluate the prediction performance.

Required data:
    Historical Stock Prices for Nvidia: Collected over the past several months or years, including daily closing prices and trading volumes.
    GPU Demand Data: Data reflecting the global demand for Nvidia GPUs over the past few years.
    Market Performance Indicators: General market indicators, such as the S&P 500 index, to account for market-wide effects on Nvidia stock prices.

Expected outcome:
    Predicted Stock Prices: The model will generate predicted stock prices for Nvidia over a future period (e.g., next 5 days).
    Comparison with Actual Data: The predicted stock prices will be compared to the actual stock prices to measure accuracy.
    Visualizations: A plot showing the predicted stock prices overlaid on the actual stock prices, allowing for visual comparison of the model’s performance.
    Model Performance Metrics: The accuracy of the model will be reported using metrics such as Mean Squared Error (MSE) or Mean Absolute Error (MAE).   
