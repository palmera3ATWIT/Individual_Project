### Individual_Project
Data Science Fundamentals Individual Research Project
## Introduction
For my individual Data Science project, I did a statistical analysis of the stock market. The three questions I decided to look into are:
1)  What stocks in the tech sector have the closest relationship?
2)  What holiday produces the most stock growth?
3)  What time duration of options produces the most profit?

I decided to look into stocks, because there is a lot of data, and companies spend lots of money to create algorithms to predict stock prices and stock movement, I don't expect to make a million-dollar algorithm here, I am just interested in what goes into stock analysis and prediction.

## Data Selection
For most of the stock data, I will be using Yahoo Finance, which allows users to directly create a CSV for any stock with excellent historical stock data. For supplementary data on index funds like the S&P 500 and the NASDAQ I used Wall Street Journal historical stock data, and tradytics which has historical options data from the past 3 months.

## Methods
1) To find what tech stocks have the strongest relationship with each other, I first downloaded the CSV files for the top 10 tech stocks. I decided to use a correlation matrix so that I could see which stocks had the closest correlation. Each of the CSV files had information on the date, opening price, high, low, closing price, adjusted close, and volume of stocks traded every day that stocks are traded for the last year, as of 3/28/2024. Since I took this stock data all on the same day, I didn't need to worry about the dates not aligning. I used the correlation matrix to find which stocks had the highest correlation for each of these stats. After Finding the pair of stocks with the overall highest correlation, I then wanted to see If I could predict the adjusted closing price of one stock using the opening price, high, low, closing price, adjusted close, and volume of the other. For this, I used sklearn and linear regression to find the line of best fit on this data set. I trained the model with 80% of my data since that seems to be the standard and tested it with the rest. I then plotted the graph and got the coefficients for each of the variables to make the equation for the line of best fit.

2) To measure the relation between holidays and stock growth, and see which holiday produces the most stock growth I will use historical data for index funds such as the S&P-500 and the NASDAQ and find the mean highs, lows, and closing prices within a timeframe of 1 week before and after the holiday. To do this, first I created a dictionary that stores the dates and names of the holidays. I decided on Christmas, Father's Day, Mother's day, and Thanksgiving. Then I set a range of 7 days to see the week before and after the holiday. Then I looped over the dictionary of holidays, each time calculating the mean between the range of dates for both sets and adding it to a list of the means. Then I calculated the yearly mean for both of the stocks using the closing price data. Using that value, I looped over the list of means and subtracted the total mean from the holiday mean for each data set, then added them together to see the total growth. After finding the holiday with the highest total growth, I used linear regression to predict the "Close" of the stock based on how many days until that holiday, within the month of the holiday. I then plotted a graph with both data sets and got the coefficients for days until the holiday to find a line of best fit.
  
3) An option is a type of financial contract that gives the buyer the right, but not the obligation, to buy or sell an asset (such as a stock) at a predetermined price (called the "strike price") within a specified period (until the "expiration date"). There are two main types of options: Call Options which the buyer the right to buy the underlying asset at the strike price. In other words, if you buy a call option, you're betting that the price of the asset will go up. Or a Put Option which gives the buyer the right to sell the underlying asset at the strike price. If you buy a put option, you're betting that the price of the asset will go down. I decided to focus on call options because I wanted to predict if the price of a stock would go up. To find what option duration returns the most profit, I gathered data from Tradytics and created a separate data set that contains only call option data. From there I narrowed down the set further to only options that expire in 2024 because the data set has specific dates for calls that expired this year as opposed to just a month and a year. Then I created a column for the duration, which just calculates the expiration date - the date purchased, and a column for profit. This uses an if statement to check if the price of the stock when the data was taken, is greater than the price they bought it at then, the profit is the current price of the stock - the price they bought it at - the bid/ask, which is essentially an average of the highest a buyer is willing to pay for and the lowest the seller is willing to sell for. From there I trained a model to predict profit, using Duration, implied volatility, which is a measure of expected future volatility of the underlying asset's price, theta, which measures the decline in value of an option as time passes, and delta, which measures the sensitivity of the asset being bought. I then plotted the data with a line of best fit and calculated the r-squared value and equation for that line.
## Results
1: Stock Correlation) After finding the correlation values for each of the variables(opening price, high, low, closing price, and adjusted close), I decided to ignore volume because none of them had a correlation coefficient of over .44 which means the volumes of the 10 stocks are not strongly correlated. There was a clear correlation between AMD the chip manufacturer, and CRM otherwise known as Salesforce, which is a company that specializes in customer relations and providing customer data for companies to analyze. I wasn't sure why but after doing some research, it appears that Salesforce uses AMD GPUs which could be why their stocks are closely related. For opening price they had a correlation coefficient of .9627, for high it was 9632, for low it was .9629, for closing price it was .9635, and for adjusted closing price it was .9635. When modeling the linear regression, I used the opening price, high, low, closing price, adjusted close, and volume of AMD to predict the adjusted close of CRM because CRM has a higher stock price. The plot I got after performing linear regression and training is shown below:

![image](https://github.com/palmera3ATWIT/Individual_Project/assets/90588963/0e374e0f-069b-45ba-9508-df9b63c0cf38)


The equation I found for the line of best fit was: CRM Adjusted Closing Price = (0.6643517902508947 * Open) + (0.2823298211818703 * High) + (-1.0673847275309807 * Low) + (0.6109839623164908 * Close) + (0.6109839623164904 * Adj Close) + (-1.4448281075441292e-07 * Volume) + 99.7633936525906.

The R-squared value for this equation is .93 which means a large portion of the variability in the adjusted closing price of CRM can be explained by the opening price, high, low, closing price, adjusted close, and volume of AMD.

2: Holiday Stock Growth) Unsurprisingly, Christmas was the holiday that produced the most growth within a week range before and after. During Christmas, there was a total 12% growth in mean compared to the yearly mean. This is expected since Christmas is heavily associated with spending money, to buy gifts for friends and family. The plot I created with the linear regression model is shown below:

![image](https://github.com/palmera3ATWIT/Individual_Project/assets/90588963/df91634a-04b4-4e6f-9e91-5bc1ce43d1cf)

The equations I found for the lines of best fit are:
S&P 500 Close = -10.64964726631394 * Days Until Christmas + 4798.693571428571
NASDAQ Close = -43.30615520282186 * Days Until Christmas + 15154.459761904764

And the R-squared values I found for the lines of best fit are:
SP500 R-squared: 0.7603686714441411
NASDAQ R-squared: 0.8584980174914311

Overall the line of best fit for the NASDAQ seems to more accurately predict the closing price than the line of best fit for the S&P 500. The graph trends downward for both stocks, likely because more people tend to buy gifts early in December to make sure they arrive in time for Christmas.

3: Option Time duration and Profit) Overall I found no correlation between duration and call profit, the plot of the data can be seen below:

![image](https://github.com/palmera3ATWIT/Individual_Project/assets/90588963/36debf04-8f82-4ea6-b29d-3fc126dbc783)

The quation of the line of best fit: Profit = (-0.011379173374003694 * Duration) + (0.004541836266787091 * Ivol) + (-7.046599174713427 * Delta) + (1.7946513804295197 * Theta) + 0.8807070237599519

The R-squared value: 0.14277088787593006

## Discussion
Overall, I found that:
1) AMD and CRM are the 2 closest related tech stocks in the top 10 tech stocks, and the adjusted closing price of CRM can be very accurately predicted using the opening price, high, low, closing price, adjusted close, and volume of AMD.

2) Christmas is the holiday that produces the most growth in the S&P 500 and the NASDAQ. Using days until Christmas can be used to semi-accurately calculate the closing price of the 2 stocks, however, the variability in the NASDAQ is slightly more predictable by the equation for its line of best fit.

3) Option call duration has little to no correlation to the profit of a call.

In the future, I would like to focus on my solutions to questions 2 and 3. For question 2, there is a lack of data points because I only used the data from one month, and stocks aren't traded every day. To get more accurate equations, I would use more historical data for December, perhaps for the past 10 years instead of the past year. However, at that point, pretty much all stocks have risen since 2014, so it might skew the data. For question 3, I would like to learn more about the options market, to get a deeper understanding of the statistics so that I can choose proper variables to predict the profit of an option. Overall this was a good experience using sklearn to train and plot linear regression models, and in the future, I would like to look into different regression models to see which ones would give me the best predictions.

 
