import os
import csv

# path to pull data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

month_count = 0
net_profit = 0

with open(csvpath, ) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        month_count = month_count + 1
        #net_profit = net_profit + int(row["Profit/Losses"])

# the minus one is to account for the header
print(f"Total Months: {month_count-1}")