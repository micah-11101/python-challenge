import csv
import os  

#define Variables
Months = 0
TotalMoney = 0
Average = 0
GreatestIncr = 0
GreatestIncrText = " "
GreatestDecr = 0
GreatestDecrText = " "
AvgChange = 0.0
LRowValue = 0

#set directory location    
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#opens csv from directory containing main.py
with open('./Resources/budget_data.csv') as csvfile:
    resourceReader = csv.reader(csvfile, delimiter=",")
    #skips the header
    csv_header = next(resourceReader)

    #iterates through each row in the csv
    for row in resourceReader:
        Months = Months + 1
        TotalMoney = TotalMoney + int(row[1])

        # if statement is used to prevent comparing the value to the intially set value
        if LRowValue != 0:
            #combines the change values before calculating Avg
            AvgChange = AvgChange + (int(row[1]) - int(LRowValue))
        #sets the last row value to current value for the next iteration
        LRowValue = row[1]
        #checks if number is greater than current value then formats the output
        if int(row[1]) > GreatestIncr:
            GreatestIncr = int(row[1])
            GreatestIncrText = row[0] + " ($" + row[1] + ")"
        #checks if number is less than current value then formats the output
        if int(row[1]) < GreatestDecr:
            GreatestDecr = int(row[1])
            GreatestDecrText = row[0] + " ($" + row[1] + ")" 


#calculates average change
AvgChange = AvgChange / Months
#opens/creates txt file 
r = open("./Analysis/FinanacialAnalysis.txt","w+")
#prints outcome of analysis loop
print("Financial Analysis \n")
print("------------------------------- \n")
print(f"Total Months: {Months} \n")
print(f"Total: ${TotalMoney} \n")
print(f"Average Change: ${AvgChange:.2f} \n")
print(f"Greatest Increase In Profits: {GreatestIncrText} \n")
print(f"Greatest Decrease In Profits: {GreatestDecrText} \n")
#writes outcome to txt file
print("Financial Analysis \n", file=r)
print("------------------------------- \n", file=r)
print(f"Total Months: {Months} \n", file=r)
print(f"Total: ${TotalMoney} \n", file=r)
print(f"Average Change: ${AvgChange:.2f} \n", file=r)
print(f"Greatest Increase In Profits: {GreatestIncrText} \n", file=r)
print(f"Greatest Decrease In Profits: {GreatestDecrText} \n", file=r)


 