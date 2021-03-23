# Banking and Election Polling with Python

## PyBank

# Background
When executed, the script will analyze the financial records of the given company's 'budget_data.csv'
The dataset is composed of two columns: `Date` and `Profit/Losses`.

* Data Analysis
The script will pull data from the csv file mentioned above, and do the following:
    * Total number of months included in the dataset
    * the net amount of the P&L over the entire period
    * calculate the P&L delta over the entire period, and then calculate the average of all the deltas
    * calculate greatest increase in profits (date and amount) over the entire period
    * calculate greatest decrease in losses (date and amount) over the entire period
# Result
The script outputs a text file 'Financial_Analysis.txt' which contains the below:

    Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1,926,159)
  Greatest Decrease in Profits: Sep-2013 ($-2,196,167)


## PyPoll

# Background
When executed, the script will analyze the votes of a small rural town election results which is given in 'election_data.csv'. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.

# Data Analysis
The script will pull data from the csv file mentioned above, and do the following:
    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote.

# Result
The script outputs a text file 'election_results.txt' which contains the below:
Election Results
---------------------------------------
Total Vote: 3521001
---------------------------------------
O'Tooley: 2.999999147969569% (105,630)
Khan: 63.00001050837531% (2,218,231)
Li: 13.999996023857989% (492,940)
Correy: 19.999994319797125% (704,200)
---------------------------------------
The winner is: Khan
---------------------------------------
