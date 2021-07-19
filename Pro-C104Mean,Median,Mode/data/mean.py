import csv

with open ("D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C104Mean,Median,Mode/data/SOCR-HeightWeight.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    data.append(float(n_num))

n=len(data)
total=0

for x in data:
    total += x

mean=total/n

print("Mean (Average) of the data is ->", mean)