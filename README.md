### Individual_Project
Data Science Fundamentals Individual Research Project
## Introduction
For my individual Data Science project, I decided to do a statistical analysis of the stock market. The three questions I decided to look into are:
1)  What stocks in the tech sector have the closest relationship?
2)  What holiday produces the most stock growth?
3)  What time duration of options produces the most profit?

I decided to look into stocks, because there is alot of data, and companies spend lots of money to create algorithms to predict stok prices and stock movement, I don't expect to create a million dollar algorithm here, I am just interested in what goes into stock analysis and predicion.

## Data Selection
For most of the stock data, I will be using yahoo finance, which allows users to directly create a csv for any stock with very good historical stock data. For supplementary data(for options specificaly), I will be using tradytics which has historical options data for the past 3 months.

## Methods
1) To find what tech stocks have the strongest relationship with eachother, I first downloaded the CSV files for the top 10 tech stocks. I decided to use a correlation matrix so that I could see which stocks had the closest correlation. Each of the CSV files had information on the date, opening price, high, low, closing price, adjusted close and volume of stocks traded every day that stocks are traded for the last year, as of 3/28/2024. Since I took this stock data all on the same day, I didn't need to worry about the dates not aligning. I used the correlation matrix to find which stocks had the highest correlation for each of these stats. After Finding the pair of stocks with the overall highest correlation, I then wanted to see If I could predict the adjusted closing price of one stock using the opening price, high, low, closing price, adjusted close and volume of the other. For this I used sklearn and linear regresson to find the line of best fit on this data set. I trained the model with 80% of my data since that seems to be the standard and tested it with the rest. I then plotted the graph, and got the coefficients of for each of the variables to make the equation for the line of best fit.
2) To measure the relation between holidays and stock growth, and see which holiday produces the most stock growth I will use Yahoo Finance to get historical data for market indicators such as the S&P-500 and the NASDAQ-100 and find the mean highs, lows, and closing prices within a timeframe of 1 week before and after the holiday. For the holidays, I will focus on holicdays associated with spending money e.g.(Christmas, Valentines, Patriots day, ect.).
3) To find what option duration returns the most profit, I will use tradytics to plot what options trades were profitable, from there, I will use the time data to separate options trades into week long segments e.g.(1-week, 2-weeks, ... ,12-weeks(3 months)). Then I will see which segments have the most profitable trades, and the realtion between trade duration and trade profit.

## Results
1) After finding the correlation values for each of the variables(opening price, high, low, closing price, and adjusted close), I decided to ignore volume because none of them had a correlaiton coefficient of over .44 which means the volumes of the 10 stocks are not strongly correlated. There was a clear correlation between AMD the chip manuafaturer, and CRM otherwise known as Salesforce, which is a company that specializes in customer relations and provinding customer data for companies to analyize. I wasn't sure why but after doing some research, it appears that Salesforce uses AMD GPUs which could be why thier stocks are closly related. For opening price they had a correlation coeffiecient of .9627, for high it was 9632, for low it was .9629, for closing price it was .9635, and for adjusted closing price it was .9635. When modeling the linear regression, I used the opening price, high, low, closing price, adjusted close and volume of AMD to predict the adjusted close of CRM because CRM has the higher stock price. The plot I got after performing linear regression and training is shown below:
![Alt text](relative%20path/to/AMD_CRM_PREDICTION.jpg?raw=true "Title")
The equation I found for the line of best fit was: CRM Adjusted Closing Price = (0.6643517902508947 * Open) + (0.2823298211818703 * High) + (-1.0673847275309807 * Low) + (0.6109839623164908 * Close) + (0.6109839623164904 * Adj Close) + (-1.4448281075441292e-07 * Volume) + 99.7633936525906
The R-sqared value for this equation is .93 which means a large portion of the variabilty in the adjusted closing price of CRM can be explained by the opening price, high, low, closing price, adjusted close and volume of AMD.
## Discussion
