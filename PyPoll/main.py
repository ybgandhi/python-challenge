# Python prgoram for PyPoll
#* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#  * The total number of votes cast
#  * A complete list of candidates who received votes
#  * The percentage of votes each candidate won
#  * The total number of votes each candidate won
#  * The winner of the election based on popular vote.
#* As an example, your analysis should look similar to the one below:
#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
import csv
PyPoll_csv = os.path.join("Resources","election_data.csv")
# set lists 
list_candidate = []
unique_candidate = []
count_vote = []
percent_vote = []
#set counter
counter = 0

#start script via with loop by opening csv
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #start for loop
    for row in csvreader:
        counter = counter + 1
    #add candidate to candidate list
        list_candidate.append(row[2])
    #establish a set for unique names
    for a in set(list_candidate):
        unique_candidate.append(a)
        # b is total votes for the candidate by using count function
        b = list_candidate.count(a)
        # add the value to the count votes list
        count_vote.append(b)
        # c is % of total vote count by diving 'b' with counter and then multiplying 100 for percent
        c = (b/counter)*100
        # add % to percent vot list
        percent_vote.append(c)
    # determine max votes from vote count list    
    votes_max = max(count_vote)
    # determine the winnter 
    winning_candidate = unique_candidate[count_vote.index(votes_max)]
#print results
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(counter))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(percent_vote[i]) +"% (" + str(count_vote[i])+ ")")
print("-------------------------")
print("The winner is: " + winning_candidate)
print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(counter) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(percent_vote[i]) +"% (" + str(count_vote[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winning_candidate + "\n")
    text.write("---------------------------------------\n")