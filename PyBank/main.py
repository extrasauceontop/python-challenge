# Import Dependencies
import os
import csv

# Set dummy variables
counter = 0
totCount = 0
totChanges = 0
greatestChange = 0
baddestChange = 0

moneys = []
csvRows = []
profitChanges = []

dict_to_csv = {}

# Set file Path
read_file = os.path.join("budget_data.csv")

# Open and read file data
with open(read_file, "r", newline = "") as pyBankFile:

    # Set CSV Reader
    csvreader = csv.reader(pyBankFile, delimiter = ',')

    # Count number of rows and subtract 1 for the header to get total months
    # Also, put rows into a list for later analytics fun
    for row in csvreader:
        counter = counter+1
        csvRows.append(row)

#---------------------------------------------------------------------------------------------------------

# Remove those pesky headers
csvRows.pop(0)
    
totMonths = counter-1

dict_to_csv["Total Months"] = totMonths

#---------------------------------------------------------------------------------------------------------

# Solve total profit/loss by summing the entire second column
# I wish I could use pandas for this, but I think that would be cheating..
# Also, I'm going to put the moneys into a list for easy referncing here
for row in csvRows:
    money = int(row[1])
    totCount = totCount + money
    moneys.append(money)

dict_to_csv["Total"] = totCount

#---------------------------------------------------------------------------------------------------------

# Calculate Average Changes

# First, get the changes into a list
for item in moneys:
    index = moneys.index(item)
    previousIndex = index-1
    if index != 0:
        change = moneys[index]-moneys[previousIndex]
        profitChanges.append(change)

# Now, sum the changes
for item in profitChanges:
    totChanges = totChanges + item

# And now get the average
averageChanges = totChanges/(totMonths-1)

dict_to_csv["Average Change"] = averageChanges

#----------------------------------------------------------------------------------------------------------

# Find the greatest increase in profits, and the index for future use
for item in profitChanges:
    if item > greatestChange:
        greatestChange = item
        greatestChange_index = profitChanges.index(item)

# Now get the month to correspond
greatestRow = csvRows[greatestChange_index+1]
greatestMonth = greatestRow[0]

dict_to_csv["Greatest Increase in Profits"] = greatestChange

#---------------------------------------------------------------------------------------------------------

# Rinse and repeat but in the opposite direction

for item in profitChanges:
    if item < baddestChange:
        baddestChange = item
        baddestChange_index = profitChanges.index(item)

# Now get the month to correspond
baddestRow = csvRows[baddestChange_index+1]
baddestMonth = baddestRow[0]

dict_to_csv["Greatest Decrease in Profits"] = baddestChange

# Set output file path
write_file = os.path.join("output.csv")

for key in dict_to_csv:
    print(key + ": " + str(dict_to_csv[key]))

with open(write_file, "w", newline = '') as newfile:
    csvwriter = csv.writer(newfile)
    for key, value in dict_to_csv.items():
        csvwriter.writerow([key, value])