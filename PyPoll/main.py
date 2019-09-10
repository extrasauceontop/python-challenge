# Import Dependencies
import os
import csv
from collections import Counter

# Set dummy variables
winner = 0

candidates = []
finalList = []
firstList = []

finalDict = {}

# Set file Path
read_file = os.path.join("election_data.csv")

# Open and read file data
with open(read_file, "r", newline = "") as pyPollFile:
    
    # Set CSV Reader
    csvreader = csv.reader(pyPollFile, delimiter = ',')

    for row in csvreader:
        # We gonna put those columns in their own distinct lists. Make life easier
        candidates.append(row[2])

# Remove headers
candidates.pop(0)

# Get total votes using the len function on one of the lists
totVotes = len(candidates)

firstList.append("Total Votes")
firstList.append(totVotes)

# Count the amount of occurences for each candidate in the candidates list
countList = [[x,candidates.count(x)] for x in set(candidates)]

# Find the winner
for item in countList:
    candidate_votes = item[1]
    if item[1] > winner:
        winner = item[1]
        winnerList = item

# Create Final List for easy printing and moving to text file
finalList.append(firstList)

for item in countList:
    finalList.append(item)

# Get percentages for each candidate
for item in finalList:
    if finalList.index(item) != 0:
        candidateVotes = item[1]
        candidatePercent = (candidateVotes/totVotes)*100
        item.append(str(round(candidatePercent,3)) + "%")

# Print relevant information
print(" ")
print("Election Results")
print("-------------------------")
for item in finalList:
    if finalList.index(item) == 0:
        print(item[0] + " " + str(item[1]))
        print("-------------------------")
    else:
        print(item[0] + ": " + item[2] + " (" + str(item[1]) + ")")


print("-------------------------")
print("Winner: " + winnerList[0])
print(" ")


# Write a CSV
write_file = os.path.join("output.csv")

with open(write_file, "w", newline = '') as newfile:
    csvwriter = csv.writer(newfile)
    for item in finalList:
        csvwriter.writerow(item)
    csvwriter.writerow(["Winner", winnerList[0]])