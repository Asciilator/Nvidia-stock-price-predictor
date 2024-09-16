i. a brief description of the project

ii. the algorithm / library / methods that you want to use

iii. any data that you might need

iv. the expected outcome

5. Statistical predictions (Simple):
For given real-world data, retrieve a statistical model. Compare the performance of the statistical prediction when provided inputs not seen by the statistical model before. Plot the prediction overlaid on actual data.

Given annual growth in global GDP and that of the US, predict the price of the iPhone for September 2024.

For autumn and winter, given the amount of solar radiation and the temperature recorded in the Netherlands in the past 5 days, predict the rainfall for the next 2 days.

Project description:
A model, which is programmed in Python, will be built, that predicts potential outcomes for real-world phenomena based on real-world data. 
It will do so by retrieving statistical models, comparing their performance on unseen inputs and visualizing predictions, which are overlaid with the data to evaluate its accuracy. 
The first application of the model will be to predict the Iphone price for September 2024 based on global GDP growth and US GDP growth.
The second application of the model will be to predict the rainfall for the next two days during autumn and winter in the Netherlands, based on solar radiation and temperature data from the past five days.

Algorithm/library/methods:
Linear Regression or Time Series Analysis (for example ARIMA or SARIMA) will be used to predict the Iphone price and the Decision Tree or Long Short-Term Memory networks to predict rainfall. 
As for the libraries, scikit-learn will be used for regression models and random forests. 
The Statsmodels library will be used for the time series analysis.
Tensorflow or Keras library will be used for deep learning methods.
Matplotlib and/or seaborn will be used to visualize the (predicted) data.

Required data:
In order to predict the IPhone price, the historical Iphone prices, global GDP growth data and US GDP growth data will be collected.
For the rainfall prediction histrorical weather data from the Netherlands regarding solar radiation and temperature measurements from the past 5 days is required.

Expected outcome:
Visual plots will be obtained from the predicted data and the actual data for visual comparison. The predicted Iphone price will probably predict the actual price poorly, since global GDP the GDP of the US alone do not influence the Iphone price to such great extent. The model that predicts the rainfall in the Netherlands will most probably reach an accuracy under 50%, since temperature measurements and solar radiation alone are not on their own determening factors for rainfall. Moreover, for a more accurate rainfall prediction, data from way more than 5 days would be needed.       
