import csv

pattern = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    # loop for each row in the file
    for row in data:
        #print(row)
        pattern.append(row[0])
    for i in pattern:
        print(i)