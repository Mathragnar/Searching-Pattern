import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    # loop for each row in the file
    for row in data:
        print(row)