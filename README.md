### Individual_Project
Data Science Fundamentals Individual Research Project
## Introduction
For my individual Data Science project, I decided to do a statistical analysis of the stock market. The three questions I decided to look into are:
1)  What stocks in the tech sector have the closest relationship?
2)  What holiday produces the most stock growth?
3)  What time duration of options produces the most profit?

## Data Selection
For most of the stock data, I will be using yahoo finance, which allows users to directly create a csv for any stock with very good historical stock data. For supplementary data(for options specificaly), I will be using tradytics which has historical options data for the past 3 months.

## Methods
1) To find what tech stocks have the strongest relationship with eachother, I will use linear regression with the top 10 to 20 stocks with the highest market cap and plot their relationship using the scikit library in python based on factors like: Open, High, Low, Close, Adj Close and Trade Volume.
2) To measure the relation between holidays and stock growth, and see which holiday produces the most stock growth I will use Yahoo Finance to get historical data for market indicators such as the S&P-500 and the NASDAQ-100 and find the mean highs, lows, and closing prices within a timeframe of 1 week before and after the holiday. For the holidays, I will focus on holicdays associated with spending money e.g.(Christmas, Valentines, Patriots day, ect.).
3) To find what option duration returns the most profit, I will use tradytics to plot what options trades were profitable, from there, I will use the time data to separate options trades into week long segments e.g.(1-week, 2-weeks, ... ,12-weeks(3 months)). Then I will see which segments have the most profitable trades, and the realtion between trade duration and trade profit.

## Results

## Discussion
