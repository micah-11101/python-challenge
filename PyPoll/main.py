import csv
import os 

#define variables
TotalVotes = 0
CanidateNames = []
VotesList = []
PercentageList = []
winner = ""
winnerNum = 0
oline = "--------------------------- \n"

#set directory location  (os.path.join would not work when running the script in the python-challenge folder) 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#opens csv from directory containing main.py
with open('./Resources/election_data.csv') as csvfile:
    resourceReader = csv.reader(csvfile, delimiter=",")
   
    #skips header since we dont use it
    csv_header = next(resourceReader)

    #iterates through every row in the csv
    for row in resourceReader:
        TotalVotes = TotalVotes + 1
        #checks if the canidate name has been stored yet and creates a value of 0 for their vote count 
        if row[2] not in CanidateNames:
            CanidateNames.append(row[2])
            VotesList.append(int(0))
        #loops through the Canidate list to see which one is matching to the current csv row
        for num,val in enumerate(CanidateNames):
            if row[2] == CanidateNames[num]:
                #adds one to the vote count if the names are matching
                VotesList[num] = VotesList[num] + 1
                
#for loop to calculate percentage of votes and winner
for num,val in enumerate(VotesList):
    PercentageList.append((float(VotesList[num])/TotalVotes)*100)

    if VotesList[num] > winnerNum:
        winnerNum = VotesList[num]
        winner = CanidateNames[num]

#print outcome
print(f"Election Results\n{oline}")
print(f"Total Votes: {TotalVotes}\n{oline}")
#for loop so that this code works with more names
for num,val in enumerate(CanidateNames):
    print(f"{val}: {PercentageList[num]:.3f}% ({VotesList[num]}) \n")
print(f"{oline}Winner: {winner}\n{oline}")

#creates txt file for analysis
r = open("./Analysis/ElectionResultAnalysis.txt","w+")
#writes the outcome to txt file
print(f"Election Results\n{oline}", file=r)
print(f"Total Votes: {TotalVotes}\n{oline}", file=r)
#for loop so that this code works with more names
for num,val in enumerate(CanidateNames):
    print(f"{val}: {PercentageList[num]:.3f}% ({VotesList[num]}) \n", file=r)
print(f"{oline}Winner: {winner}\n{oline}", file=r)