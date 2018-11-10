import os
import csv

# Path to collect data from the resources folder
BudgetdataCSV = os.path.join("..","PyBank","Resources","budget_data.csv")
fileId =open('pybank.txt', 'w')

#deine the function and have it accept the PyBank data
def financialAnalysis(PyBankDta):
    #The total number of months included in the data set
    TotalMonth =0
    NetProfit = 0
    change = 0
    n = 0
    greatestInc = 0
    greatestDec = 0
    greatestDate = ""
    for row in PyBankDta:
        # count the number of unique months
        TotalMonth+=1

        # Amount of profit/loss over the enire period
        NetProfit+=int(row[1])

    # Average change in profit/loss between months over the entire period
        if n == 0:
            firstMonth = int(row[1])
            n += 1
        else:
            secondMonth = int(row[1])
            difference = secondMonth - firstMonth

            change += difference
            n += 1
            firstMonth = secondMonth
       # Greatest increase  in profit over the entire period
            if difference > greatestInc:
                greatestInc = difference
                greatestDate = row[0]
        # Greatest decrease in profit over the entire period
            if difference < greatestDec:
                greatestDec = difference
                greatestDate = row[0]

    print("Financial Analysis")
    fileId.write("Financial Analysis")

    print("........................................")
    fileId.write("........................................")
    print(f" Total Months {TotalMonth}")
    fileId.write(f" Total Months {TotalMonth}")
    print(f" NetProfit {NetProfit}")
    fileId.write(f" NetProfit {NetProfit}")
    print(f" Average change {change / (n-1)}")
    fileId.write(f" Average change {change / (n-1)}")
    print(f"Greatest increase in profit: {greatestDate} ({greatestInc})")
    fileId.write(f"Greatest increase in profit: {greatestDate} ({greatestInc})")
    print(f"Greatest decrease in loss: {greatestDate} ({greatestDec})")
    fileId.write(f"Greatest decrease in loss: {greatestDate} ({greatestDec})")

    fileId.close()

# the total net amount of profit/losses over entire period

#Read the csv file
with open(BudgetdataCSV,'r') as csvfile:
    #split the data on commas
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    financialAnalysis(csvreader)
