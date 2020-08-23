import os
import csv

# path to pull data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

vote_count = 0
candidates = []
khan = []
correy = []
li = []
otooley = []

# same as the other, csv to read
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip first row, header like in the other
    csv_header = next(csvreader)
    #loop through the data
    for row in csvreader:
        #number of votes looping through rows and adding
        vote_count = vote_count + 1
        candidates.append(row[2])

    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_count = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_count = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_count = len(li)
        else:
            otooley.append(candidates)
            otooley_count = len(otooley)

print(f"Total Votes: {vote_count}\n",
f"Khan: {100*khan_count/vote_count}%\n",
f"Correy: {100*correy_count/vote_count}%\n",
f"Li: {100*li_count/vote_count}\n",
f"O'Tooley: {100*correy_count/vote_count}\n")
