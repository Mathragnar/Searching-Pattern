import csv

count = 0

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    # loop for each row in the file
    for row in data:
        #print(row)
        for number, i in enumerate(row):
            #print(number)
            if number == row[i]:
                print(f"Found {number} in row {row}")
