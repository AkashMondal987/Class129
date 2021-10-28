import csv
data = []
with open("dataset_2.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
headers = data[0]
planetData = data[1:]
for datapoint in planetData:
    datapoint[2] = datapoint[2].lower()
planetData.sort(key = lambda planetData:planetData[2])
with open("dataset_2_sorted.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetData)