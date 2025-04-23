from collections import Counter

numbers_unorded = [
    -0.25, 0.75, 1, 0.13, 0.45, 0.75, -0.80, -0.25, 0.50, 1,
    1.55, 0.75, -1.10, -0.25, 0.05, 0.75, -0.62, 1, 0.99, -0.01,
    0.75, 1.20, -0.25, -0.33, 0.45, 0.20, 0.75, 0.88, -1.50, -0.95
]

counter = Counter(numbers_unorded)

ordered_numbers = sorted(counter.items(), key=lambda item: item[1], reverse=True)

for number, quantity in ordered_numbers:
    print(f"{number} appears {quantity} time{'s' if quantity > 1 else ''}")

# This code counts the occurrences of each number in the list and sorts them in descending order.
# It then prints each number along with its count, using the correct pluralization for "time".
# The code is a simple example of how to use the Counter class from the collections module to count occurrences of items in a list.
# The code also demonstrates how to sort the counted items based on their frequency.
# The code is a simple example of how to use the Counter class from the collections module to count occurrences of items in a list.
# The code also demonstrates how to sort the counted items based on their frequency.
# The code is a simple example of how to use the Counter class from the collections module to count occurrences of items in a list.
# The code also demonstrates how to sort the counted items based on their frequency.
# The code is a simple example of how to use the Counter class from the collections module to count occurrences of items in a list.