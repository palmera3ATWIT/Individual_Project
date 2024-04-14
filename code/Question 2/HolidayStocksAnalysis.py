import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")


# Load data from the CSV files
SP500 = pd.read_csv('S&P500.csv', parse_dates=['Date'])
NASDAQ = pd.read_csv('NASDAQ.csv', parse_dates=['Date']) 

SP500['Date'] = pd.to_datetime(SP500['Date'])
NASDAQ['Date'] = pd.to_datetime(NASDAQ['Date'])

# Create a dictionary that contains the holidays I'm analyizing(Chrismas, Father's day, Mother's day, and Thanksgiving)
holidays = {datetime(2023, 12, 25): "Christmas", datetime(2023, 6, 18): "Father's Day"
            , datetime(2023, 5, 14): "Mother's Day",datetime(2023, 11, 23): "Thanks Giving"}

# Create a range of a week to see dates a week before and after the holiday
holiday_window = timedelta(days=7)

# Calculate the mean price of the stock during the range of days and add it to the list of means
holiday_means = []
for holiday, holiday_name in holidays.items():
    start_holiday = holiday - holiday_window
    end_holiday = holiday + holiday_window
    sp500_holiday_data = SP500[(SP500['Date'] >= start_holiday) & (SP500['Date'] <= end_holiday)]
    nasdaq_holiday_data = NASDAQ[(NASDAQ['Date'] >= start_holiday) & (NASDAQ['Date'] <= end_holiday)]
    sp500_mean = sp500_holiday_data[[' Open', ' High', ' Low', ' Close']].mean()
    nasdaq_mean = nasdaq_holiday_data[[' Open',' High', ' Low', ' Close']].mean()
    holiday_means.append([holiday_name, sp500_mean, nasdaq_mean])

# Find the yearly mean for the S&P 500 and the NASDAQ
yearly_sp500_mean = SP500[' Close'].mean()
yearly_nasdaq_mean = NASDAQ[' Close'].mean()

# Initialize variables to store the holiday with the highest growth and its corresponding growth value
max_growth = 0
best_holiday = None

# Loop through each holiday and calculate the growth compared to the overall mean
for holiday_data in holiday_means:
    holiday_name, sp500_mean, nasdaq_mean = holiday_data 
    sp500_growth = sp500_mean[' Close'] - yearly_sp500_mean
    nasdaq_growth = nasdaq_mean[' Close'] - yearly_nasdaq_mean
    total_growth = sp500_growth + nasdaq_growth
    if total_growth > max_growth:
        max_growth = total_growth
        best_holiday = holiday_name

print("Holiday with highest growth:", best_holiday, max_growth)

max_growth_percentage = 0
for holiday_data in holiday_means:
    holiday_name, sp500_mean, nasdaq_mean = holiday_data
    sp500_growth_percentage = ((sp500_mean[' Close'] - yearly_sp500_mean) / yearly_sp500_mean) * 100
    nasdaq_growth_percentage = ((nasdaq_mean[' Close'] - yearly_nasdaq_mean) / yearly_nasdaq_mean) * 100
    total_growth_percentage = sp500_growth_percentage + nasdaq_growth_percentage
    if total_growth_percentage > max_growth_percentage:
        max_growth_percentage = total_growth_percentage
        best_holiday_percentage = holiday_name

print("Holiday with highest growth (as percentage):", best_holiday_percentage, max_growth_percentage)


# Take only the days in december
SP500_december = SP500[SP500['Date'].dt.month == 12]
NASDAQ_december = NASDAQ[NASDAQ['Date'].dt.month == 12]

# Calculate the number of days until Christmas for each December date
SP500_december['Days_until_Christmas'] = (datetime(2023, 12, 25) - SP500_december['Date']).dt.days
NASDAQ_december['Days_until_Christmas'] = (datetime(2023, 12, 25) - NASDAQ_december['Date']).dt.days

# Filter the data to include only the days before Christmas in December
SP500_before_christmas = SP500_december[SP500_december['Days_until_Christmas'] > 0]
NASDAQ_before_christmas = NASDAQ_december[NASDAQ_december['Days_until_Christmas'] > 0]

X_SP500 = SP500_before_christmas[['Days_until_Christmas']]
y_SP500 = SP500_before_christmas[' Close']

X_NASDAQ = NASDAQ_before_christmas[['Days_until_Christmas']]
y_NASDAQ = NASDAQ_before_christmas[' Close']

# Split the data into training and testing sets using 80% to train and 20% to test
X_train_SP500, X_test_SP500, y_train_SP500, y_test_SP500 = train_test_split(X_SP500, y_SP500, test_size=0.2, random_state=0)
X_train_NASDAQ, X_test_NASDAQ, y_train_NASDAQ, y_test_NASDAQ = train_test_split(X_NASDAQ, y_NASDAQ, test_size=0.2, random_state=0)

# Train the linear regression model for both sets
model_SP500 = LinearRegression()
model_SP500.fit(X_train_SP500, y_train_SP500)

model_NASDAQ = LinearRegression()
model_NASDAQ.fit(X_train_NASDAQ, y_train_NASDAQ)

y_predicted_SP500 = model_SP500.predict(X_test_SP500)
y_predicted_NASDAQ = model_NASDAQ.predict(X_test_NASDAQ)

# Find the r squared values for each model

r2_SP500 = r2_score(y_test_SP500, y_predicted_SP500)

r2_NASDAQ = r2_score(y_test_NASDAQ, y_predicted_NASDAQ)

print("SP500 R-squared:", r2_SP500)

print("NASDAQ R-squared:", r2_NASDAQ)


# Plot S&P 500 data
plt.scatter(X_SP500, y_SP500, color='blue', label='S&P 500 Data')

# Plot NASDAQ data
plt.scatter(X_NASDAQ, y_NASDAQ, color='red', label='NASDAQ Data')

# Plot the lines of best fit
plt.plot(X_SP500, model_SP500.predict(X_SP500), color='blue', linestyle='--', label='S&P 500 Regression Line')
plt.plot(X_NASDAQ, model_NASDAQ.predict(X_NASDAQ), color='red', linestyle='--', label='NASDAQ Regression Line')

plt.title('Stock Prices vs. Days Until Christmas')
plt.xlabel('Days Until Christmas')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.show()


slope_SP500 = model_SP500.coef_[0]
intercept_SP500 = model_SP500.intercept_

slope_NASDAQ = model_NASDAQ.coef_[0]
intercept_NASDAQ = model_NASDAQ.intercept_

print(f"S&P 500 Close = {slope_SP500} * Days Until Christmas + {intercept_SP500}")
print(f"NASDAQ Close = {slope_NASDAQ} * Days Until Christmas + {intercept_NASDAQ}")