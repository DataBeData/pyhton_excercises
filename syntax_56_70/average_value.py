#Find Average Value
#Open temperatures.csv and calculate 
#the average temperature from the "Temp" column.
import csv

temps_list=[]
count_rows = 0
with open("temperatures.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        for i in row["Temperature"]:
            i = int(i)
            count_rows += 1
            temps_list.append(i)

total =sum(temps_list)
avg_temp = total / count_rows
print(avg_temp)



#version 2

temps = []

with open("temperatures.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        temps.append(float(row["Temperature"]))

average_temp = sum(temps) / len(temps)
print(f"Average temperature: {average_temp:.2f}")



#version 3

total_temp = 0
count = 0

with open("temperatures.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_temp += float(row["Temperature"])
        count += 1

average_temp = total_temp / count
print(f"Average temperature: {average_temp:.2f}")
