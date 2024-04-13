import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# List of CSV files
csv_files = ["AAPL.csv", "ACN.csv", "ADBE.csv", "AMD.csv", "AVGO.csv",
             "CSCO.csv", "ORCL.csv", "NVDA.csv", "MSFT.csv", "CRM.csv"]

# Function to read CSV and return DataFrame with the specified statistic
def read_stat(csv_file, stat):

    df = pd.read_csv(csv_file)

    stat_column = df[stat]
    
    return stat_column

stat = 'Open'

stat_df = pd.DataFrame()

# Loop over CSVs and get the desired stock, then rename the stat column to the name of the stock, for readability
for csv_file in csv_files:
    ticker = csv_file.split(".")[0]
    stat_column = read_stat(csv_file, stat)
    stat_df[ticker] = stat_column

correlation_matrix = stat_df.corr()

max_corr_value = 0
max_corr_pair = ()

# Iterate over pairs of stocks using nested for loop
for stock1 in correlation_matrix.columns:
    for stock2 in correlation_matrix.columns:
        # Make sure stock 1 does not equal stock 2
        if stock1 != stock2:
            # Get correlaiton value for stock 1 and 2
            corr = correlation_matrix.loc[stock1, stock2]
            # If this value is greater than the current highest correlation value, update it, and keep track of the pair of stocks
            if corr > max_corr_value:
                max_corr_value = corr
                max_corr_pair = (stock1, stock2)

# Print the pair with the highest correlation value
print(f"Pair with highest correlation value for {stat} is:")
print(max_corr_pair, ":", max_corr_value)