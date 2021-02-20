# Python program for PyBank
# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# * Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
# * As an example, your analysis should look similar to the one below:
#   text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
        # write a code to count unique values in column A
#  Total: $38382578
        # write a code to sum column B
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Solution:

#import os and csv
import os
import csv
# set csv file from Resource folder
PyBank_csv = os.path.join("Resources","budget_data.csv")

# create list for date, month_delta, profit
date = []
delta_month = []
profit = []
# set variables for 'with' loop
counter_month = 0
total_profit = 0
delta_profit = 0
initial_profit = 0
final_profit = 0
#start loop by opening the csv file
with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #csv file has headers already so we can skip first row
    csvheader = next(csvreader)
    #start for loop    
    for row in csvreader:
        #counter month will keep track of number months each time it loops    
        counter_month = counter_month + 1
        #to add to date list
        date.append(row[0])
        #to add to profit list
        profit.append(row[0])
        #calculate total profit
        total_profit = total_profit + int(row[1])
        #store final profit
        final_profit = int(row[1])
        #month over month profit change
        MoM_profit = final_profit - initial_profit
        #add month over month profit change to delta month list
        delta_month.append(MoM_profit)
        #calculate change in profit
        delta_profit = delta_profit + MoM_profit
        #for next loop, make final profit the new initial profit 
        initial_profit = final_profit
        #calculate average profit
        average_profit = (delta_profit/counter_month)
        #find new min and max for month from list
        max_increase_profit = max(delta_month)
        max_decrease_profit = min(delta_month)
        #store min and max from list in variable
        max_date = date[delta_month.index(max_increase_profit)]
        min_date = date[delta_month.index(max_decrease_profit)]

print("-------------------")
print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(counter_month))
print("Total Profits: $" + str(total_profit))
print("Average Change: " + "$" + str(int(average_profit)))
print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_increase_profit) + ")")
print("Greatest Dencrease in Profits: " + str(min_date) + " ($" + str(max_decrease_profit) + ")")
print("-------------------")
#with script to store text file
with open('Financial_Analysis.txt', 'w') as text:
        text.write("-------------------")
        text.write("Financial Analysis")
        text.write("-------------------")
        text.write("Total Months: " + str(counter_month))
        text.write("Total Profits: $" + str(total_profit))
        text.write("Average Change: " + "$" + str(int(average_profit)))
        text.write("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_increase_profit) + ")")
        text.write("Greatest Dencrease in Profits: " + str(min_date) + " ($" + str(max_decrease_profit) + ")")
        text.write("-------------------")