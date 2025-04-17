import csv
from collections import Counter

numbers = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    for row_index, row in enumerate(data):
        if row_index > 0:
            for number_index, number in enumerate(row):
                numbers.append(number)

counter = Counter(numbers)
ordered_numbers = sorted(counter.items(), key=lambda item: item[1], reverse=True)

for number, quantity in ordered_numbers:
    print(f"{number} appears {quantity} time{'s' if quantity > 1 else ''}")
    if quantity == 1:
        break
