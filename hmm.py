import os 
import csv

csv_path = os.path.join("Resources", "em.csv")

First = []
Last = []
Emp = []
DOB = []
with open (csv_path) as reading_obj:
    csv_reader = csv.reader(reading_obj)
    next(csv_reader)
    for row in csv_reader:
        index = row[1].find(" ")
        First_Name = row[1][: index]
        First.append(First_Name)
        Last_Name = row[1][-index :]
        Last.append(Last_Name)
        emp = row[0]
        Emp.append(emp)
        dob = row[2]
        DOB.append(dob)

year = [i.split('-')[0] for i in DOB]
# print(year)
month = [i.split('-')[1] for i in DOB]
# print(month)
days = [i.split('-')[2] for i in DOB]
# print(days)
mdy = []
qcount = 0
for i in year:
    x = str(month[qcount]) + '/' + str(days[qcount]) + '/' + str(year[qcount])
    mdy.append(x)
    qcount += 1
    if qcount == len(year):
        break
# print(mdy)

with open ("csvpractice1.csv", 'w', newline='') as practicefile:
    thiswriter = csv.DictWriter(practicefile, ["EMP ID", "First Name", "Last Name", "DOB"])
    thiswriter.writeheader()
    rcount = 0
    for row in First:
        thiswriter.writerow({"EMP ID": Emp[rcount], "First Name": First[rcount], "Last Name": Last[rcount], "DOB": mdy[rcount]})
        rcount += 1
        if rcount == len(First):
            break
