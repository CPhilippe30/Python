# Dependencies

import csv
import os

# Files to load and output
csvpath= os.path.join( "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    cvs_header= next(csvreader)


#Declaring variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

#VOTE COUNT
total_votes = (len(votes))
print(total_votes)


#Votes by Person
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

for candidate in candidates:
    if candidate == "Khan":
        khan_votes += 1
    if candidate == "Correy":
        correy_votes += 1
    if candidate == "Li":
        li_votes += 1

    else:
        otooley.append(candidates)
        otooley_votes = len(otooley)
print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)



#Percentages
khan_percent = round(khan_votes * 100.0 / total_votes , 2)
correy_percent = round(correy_votes *100.0/ total_votes, 2)
li_percent = round(li_votes *100.0/total_votes,2)
otooley_percent = round(otooley_votes *100.0/ total_votes,2)
print(khan_percent)
print(correy_percent)
print(li_percent)
print(otooley_percent)


#Winner
if khan_percent > max(correy_percent, li_percent, otooley_percent):
    winner = "Khan"
if correy_percent > max(khan_percent, li_percent, otooley_percent):
    winner = "Correy"
if li_percent > max(correy_percent, khan_percent, otooley_percent):
    winner = "Li"
else:
    winner = "O'Tooley"


#Results
print("Election Results")
print("-----------------------------------")
print("Total Votes: {0}".format(total_votes))
print("-----------------------------------\n")
print("Khan: {0}% ({1})".format(khan_percent, khan_votes))
print("Correy: {0}% ({1})".format(correy_percent, correy_votes))
print("Li: {0}% ({1})".format(li_percent, li_votes))
print("otooley: {0}% ({1})".format(otooley_percent, otooley_votes))
print("-----------------------------------" + "\n")
print("Winner: {winner}"+ "\n" )
print("-----------------------------------")



khan_votes = 0
for candidate in candidates:
    if candidate == "Khan":
        khan_votes += 1


khan_percent = round(khan_votes / total_votes * 100, 2)
print(khan_percent)
 
