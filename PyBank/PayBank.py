import os
import csv

# Path to collect data from the resources folder
BudgetdataCSV = os.path.join("..","PyBank","Resources","budget_data.csv")

#deine the function and have it accept the PyBank data
def financialAnalysis(PyBankDta):
    #The total number of months included in the data set
    TotalMonth =0
    NetProfit = 0
    change = 0
    n = 0
    for row in PyBankDta:
        # count the number of unique months
        TotalMonth+=1
        NetProfit+=int(row[1])

        if n == 0:
            firstMonth = int(row[1])
            n += 1
        else:
            secondMonth = int(row[1])
            change += (secondMonth - firstMonth)
            n += 1
            firstMonth = secondMonth

    print(f" Total Months {TotalMonth}")
    print(f" NetProfit {NetProfit}")
    print(f" Average change {change / (n-1)}")

# the total net amount of profit/losses over entire period




#Read the csv file
with open(BudgetdataCSV,'r') as csvfile:
    #split the data on commas
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)


    financialAnalysis(csvreader)
