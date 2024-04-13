from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

AMD = pd.read_csv('AMD.csv')
CRM = pd.read_csv('CRM.csv')


stats = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
# I'm using the open, high, low, close, adj close and volume from the AMD stock as independant variables
X = AMD[stats]
# And the dependent variable is the adj close of the CRM stock
y = CRM['Adj Close']

# Split data into training and testing sets using 20% of the data for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X)

# Plot data and the line of best fit
plt.scatter(predictions, y, color='blue', label='Data')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', label='Line of Best Fit')
plt.xlabel('Predicted Adjusted Closing Price')
plt.ylabel('Actual Adjusted Closing Price')
plt.title('Linear Regression: Predicted vs. Actual')
plt.legend()
plt.show()

# Get the equation of the line by iterating through the coefficients and matching them to the appropiate stat
coefficients = model.coef_
intercept = model.intercept_
equation = 'CRM Adjusted Closing Price = '
for i in range(len(stats)):
    equation += f'({coefficients[i]} * {stats[i]}) + '
equation += str(intercept)
print("Equation of the line of best fit:", equation)

# Calculate R-squared value to see the accuracy of the equation
r_squared = r2_score(y, predictions)
print("R-squared value:", r_squared)