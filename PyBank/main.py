#dependencies
import pandas as pd
import numpy as np

#create a reference for the CSV file
df=pd.read_csv('Resources/budget_data.csv')

#printing the text to format the results
print("Financial Analysis")
print("    ")
print("-------------------------------------------------------")
print("     ")

#unique values -> months
total_months=df['Date'].nunique()
print("Total Months:   ",total_months)
print("    ")

#calculating the sum of the Profit/Losses column
Total=df['Profit/Losses'].sum()
print("Total:    $",Total)
print("    ")

#creating a list and calculating the average with a for loop
lis=[]
d= df.to_numpy().tolist()
for i in range(0,len(d)-1):
    change=d[i+1][1]-d[i][1]
    lis.append(change)
    change=round(sum(lis)/len(lis),2)
lis.insert(0,0)
#creating a new column to hold the average values
df['Average change']=lis

#calculating the greatest increase and decrease from that new column with a for loop
d=df.to_numpy().tolist()
max_change=df['Average change'].max()
min_change=df['Average change'].min()
min_date=""
ma_date=""
for i in range(0,len(d)):
    if d[i][2]==max_change:
        max_date=d[i][0]
    elif d[i][2]==min_change:
        min_date=d[i][0]

#printing all the results out
print("")
print("Greatest Increase in profit : {} (${})".format(max_date,max_change))
print("")
print("Greatest Decrease in profit : {} (${})".format(min_date,min_change))
print(" ")

#creating the new text file with the result printed out
import sys
sys.stdout = open('analysis/report.txt', 'wt')
print("Financial Analysis")
print("    ")
print("-------------------------------------------------------")
print("     ")
total_months=df['Date'].nunique()
print("Total Months:   ",total_months)
print("    ")
Total=df['Profit/Losses'].sum()
print("Total:    $",Total)
print("    ")
print("Average Change: ${}".format(change))
print("  ")
print("")
print("Greatest Increase in profit : {} (${})".format(max_date,max_change))
print("")
print("Greatest Decrease in profit : {} (${})".format(min_date,min_change))
print(" ")

#Tsvetan Tsvetkov with a bit of google:)