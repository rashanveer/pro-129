import csv
dataset1 = []
dataset2 = []

with open("dataset1.csv","r")as f:
    csvReader1 = csv.reader(f)
    for row1 in csvReader1:
        dataset1.append(row1)

with open("dataset2.csv","r")as f:
    csvReader2 = csv.reader(f)
    for row2 in csvReader2:
        dataset2.append(row2)

header1 = dataset1[0]
planet_data1 = dataset1[1:]
header2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = header1 + header2
planetData = []
for index, data_row in enumerate(planet_data1): 
    planetData.append(planet_data1[index] + planet_data2[index]) 
with open("merge.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planetData)