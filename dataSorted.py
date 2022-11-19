import csv
planetData = []

with open("dataset2.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        planetData.append(row)

headers = planetData[0]
planet_data = planetData[1:]

for planetPoint in planet_data:
    planetPoint[2] = planetPoint[2].lower()

planet_data.sort(key=lambda planet_data: planet_data[2]) 
with open("dataset_2_sorted.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)