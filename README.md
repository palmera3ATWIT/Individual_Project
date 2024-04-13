### Individual_Project
Data Science Fundamentals Individual Research Project
## Introduction
For my individual Data Science project, I decided to do a statistical analysis of the stock market. The three questions I decided to look into are:
1)  What stocks in the tech sector have the closest relationship?
2)  What holiday produces the most stock growth?
3)  What time duration of options produces the most profit?

I decided to look into stocks, because there is alot of data, and companies spend lots of money to create algorithms to predict stok prices and stock movement, I don't expect to create a million dollar algorithm here, I am just interested in what goes into stock analysis and predicion.

## Data Selection
For most of the stock data, I will be using yahoo finance, which allows users to directly create a csv for any stock with very good historical stock data. For supplementary data on index funds like the S&P 500 and the NASDAQ, and tradytics which has historical options data from the past 3 months.

## Methods
1) To find what tech stocks have the strongest relationship with eachother, I first downloaded the CSV files for the top 10 tech stocks. I decided to use a correlation matrix so that I could see which stocks had the closest correlation. Each of the CSV files had information on the date, opening price, high, low, closing price, adjusted close and volume of stocks traded every day that stocks are traded for the last year, as of 3/28/2024. Since I took this stock data all on the same day, I didn't need to worry about the dates not aligning. I used the correlation matrix to find which stocks had the highest correlation for each of these stats. After Finding the pair of stocks with the overall highest correlation, I then wanted to see If I could predict the adjusted closing price of one stock using the opening price, high, low, closing price, adjusted close and volume of the other. For this I used sklearn and linear regresson to find the line of best fit on this data set. I trained the model with 80% of my data since that seems to be the standard and tested it with the rest. I then plotted the graph, and got the coefficients of for each of the variables to make the equation for the line of best fit.
2) To measure the relation between holidays and stock growth, and see which holiday produces the most stock growth I will use historical data for index funds such as the S&P-500 and the NASDAQ and find the mean highs, lows, and closing prices within a timeframe of 1 week before and after the holiday. To do this, first I created a dicitonary that stores the dates and names for the holidays. I decided on Chrismas, Father's day, Mother's day, and Thanksgiving. Then I set a range of 7 days to see the week before and after the holiday. Then I looped over the dictionary of holidays, each time calculating the mean between the range of dates for both sets and adding it to a list of the means. Then I calculated the yearly mean for both of the stocks using the closing price data. Using that value, I looped over the list of means and subtracted the total mean from the holiday mean for each data set, then added them together to see the total growth. After finding the holiday with the highest total growth, I used linear regression to predict the "Close" of the stock based on how many days untill that holiday, within the month of the holiday. I then plotted a graph with both data sets, and got the coefficients for days until the holiday to find line of best fit.
3) To find what option duration returns the most profit, I will use tradytics to plot what options trades were profitable, from there, I will use the time data to separate options trades into week long segments e.g.(1-week, 2-weeks, ... ,12-weeks(3 months)). Then I will see which segments have the most profitable trades, and the relation between trade duration and trade profit.

## Results
1) After finding the correlation values for each of the variables(opening price, high, low, closing price, and adjusted close), I decided to ignore volume because none of them had a correlaiton coefficient of over .44 which means the volumes of the 10 stocks are not strongly correlated. There was a clear correlation between AMD the chip manuafaturer, and CRM otherwise known as Salesforce, which is a company that specializes in customer relations and provinding customer data for companies to analyize. I wasn't sure why but after doing some research, it appears that Salesforce uses AMD GPUs which could be why thier stocks are closly related. For opening price they had a correlation coeffiecient of .9627, for high it was 9632, for low it was .9629, for closing price it was .9635, and for adjusted closing price it was .9635. When modeling the linear regression, I used the opening price, high, low, closing price, adjusted close and volume of AMD to predict the adjusted close of CRM because CRM has the higher stock price. The plot I got after performing linear regression and training is shown below:

![image](https://github.com/palmera3ATWIT/Individual_Project/assets/90588963/0e374e0f-069b-45ba-9508-df9b63c0cf38)


The equation I found for the line of best fit was: CRM Adjusted Closing Price = (0.6643517902508947 * Open) + (0.2823298211818703 * High) + (-1.0673847275309807 * Low) + (0.6109839623164908 * Close) + (0.6109839623164904 * Adj Close) + (-1.4448281075441292e-07 * Volume) + 99.7633936525906.

The R-sqared value for this equation is .93 which means a large portion of the variabilty in the adjusted closing price of CRM can be explained by the opening price, high, low, closing price, adjusted close and volume of AMD.

2) Unsupprisingly, Christmas was the holiday that produced the most growth within a week range before and after. During Christmas there was a total 12% growth in mean compared to the yearly mean. This is expected since Christmas is heavily associated with spending money, to buy gifts for friends and family. The plot I created with the linear regression model is shown below:

![image](https://github.com/palmera3ATWIT/Individual_Project/assets/90588963/df91634a-04b4-4e6f-9e91-5bc1ce43d1cf)

The equations I found for the lines of best fit are:
S&P 500 Close = -10.64964726631394 * Days Until Christmas + 4798.693571428571
NASDAQ Close = -43.30615520282186 * Days Until Christmas + 15154.459761904764

And the R-squared values I found for the lines of best fit are:
SP500 R-squared: 0.7603686714441411
NASDAQ R-squared: 0.8584980174914311

Overall the line of best fit for the NASDAQ seems to more accuratly predict the closeing price then the line of best fit for the S&P 500. The graph trends downward in for both stocks, likely because more people tend to buy gifts early in december to make sure they arrive in time for Christmas.

## Discussion
