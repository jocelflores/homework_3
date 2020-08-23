import os
import csv

# path to pull data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

vote_count = 0

# same as the other, csv to read
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip first row, header like in the other
    csv_header = next(csvreader)
    #loop through the data
    for row in csvreader:
        vote_count = vote_count + 1

print(f"Total Votes: {vote_count}")
