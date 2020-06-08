import os 
import csv

csv_path = os.path.join("Resources", "em.csv")

First = []
Last = []
Emp = []
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

with open ("csvpractice1.csv", 'w', newline='') as practicefile:
    thiswriter = csv.DictWriter(practicefile, ["EMP ID", "First Name", "Last Name"])
    thiswriter.writeheader()
    rcount = 0
    scount = 0
    ecount = 0
    for row in First:
        thiswriter.writerow({"EMP ID": Emp[ecount], "First Name": First[rcount], "Last Name": Last[scount]})
        rcount += 1
        scount += 1
        ecount += 1
        if rcount == len(First):
            break