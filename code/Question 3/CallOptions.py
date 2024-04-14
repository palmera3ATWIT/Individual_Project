import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


# Load the dataset
data = pd.read_csv('Trady Flow - Best Options Trade Ideas.csv')

# Convert 'Exp' column to datetime type
data['Exp'] = pd.to_datetime(data['Exp'])
data['T'] = pd.to_datetime(data['T'])

# Filter for call options expiring in 2024
call_options = data[(data['C/P'] == 'Calls') & (data['Exp'].dt.year == 2024)]

# Filter for call options expiring in 2024
call_options = call_options[call_options['Exp'].dt.year == 2024]
# Calculate the duration (time remaining until expiration) in days for call_options only
call_options['Duration'] = (call_options['Exp'] - call_options['T']).dt.days

profits = []

# Iterate over each row in the DataFrame and calculate the profit
for index, row in call_options.iterrows():
    if row['Spot'] > row['Strike']:
        profit = (row['Spot'] - row['Strike']) - row['BidAsk']
    else:
        profit = -row['BidAsk']
    profits.append(profit)

# Add the profits list as a new column the call_options DataFrame
call_options['Profit'] = profits 

# Filter out options whose profit is worse than $-20
call_options_filtered = call_options[call_options['Profit'] > -20]
X = call_options_filtered[['Duration','Ivol','Delta','Theta']]
y = call_options_filtered['Profit']  


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Evaluate the model
prediction = model.predict(X)

# Evaluate the model performance
r_squared = r2_score(y, prediction)

# Get the coefficients and intercept from the model
coefficients = model.coef_
intercept = model.intercept_

# Scatter plot of actual vs. predicted values for testing data
plt.figure(figsize=(10, 6))
plt.scatter(prediction, y, color='green', label='Testing Data')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Prediction')
plt.xlabel('Actual Profit')
plt.ylabel('Predicted Profit')
plt.title('Scatter plot of Actual vs. Predicted Profit')
plt.legend()
plt.show()

equation = 'Profit = '
for i in range(len(coefficients)):
    equation += f'({coefficients[i]} * {X.columns[i]}) + '
equation += str(intercept)

# Print the equation of the line of best fit
print("Equation of the line of best fit:", equation)
print(r_squared)