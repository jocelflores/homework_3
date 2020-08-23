import os
import csv

# path to pull data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# lists to track/store changes and the month they happen
date = []
monthly_net_list = []
profit_loss = []

month_count = 0
total_net_profit = 0
total_changes = 0
profit_1 = 0

with open(csvpath,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skips header
    csv_header = next(csvreader)

    for row in csvreader:
        # Find the net profit/losses and month count
        month_count = month_count + 1
        # Add date to list
        date.append(row[0])

        # Add net profit information to list; calculate total profit
        profit_loss.append(row[1])
        total_net_profit = total_net_profit + int(row[1])

        # month to month changes and storing values
        monthly_net = int(row[1]) - profit_1
        profit_1 = int(row[1])
        monthly_net_list.append(monthly_net)
        total_changes = total_changes + monthly_net

        #calculate average
        average_profit = (total_changes/month_count)

        # finding greatest increase and greatest decrease in the list
        greatest_increase = max(monthly_net_list)
        greatest_decrease = min(monthly_net_list)
        # match the dates to the 
        greatest_increase_date = date[(monthly_net_list).index(greatest_increase)]
        greatest_decrease_date = date[(monthly_net_list).index(greatest_decrease)]
    
# Attempted to subtract one row for header
# Header is not an integer so this method does not work with the net_profit
print(f" Total Months: {month_count}\n", 
f"Total: ${total_net_profit}\n",
f"Average Change: ${average_profit}\n",
f"Greatest Increase in Profits: {greatest_increase_date, greatest_increase}\n",
f"Greatest Decrease in Profits: {greatest_decrease_date, greatest_decrease}\n")

output = (
f"Financial Analysis\n",
f"________________________________",
f" Total Months: {month_count}\n" ,
f"Total: ${total_net_profit}\n",
f"Average Change: ${average_profit}\n",
f"Greatest Increase in Profits: {greatest_increase_date, greatest_increase}\n",
f"Greatest Decrease in Profits: {greatest_decrease_date, greatest_decrease}\n")

# Print output to text file, it prints in one line instead of several

textfile_path = os.path.join('Analysis', 'print_analysis.txt')
with open(textfile_path, 'w') as txt_file:
    txt_file.write(str(output))