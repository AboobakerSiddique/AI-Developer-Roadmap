#Problem 1 – Find the Largest Number ⭐
#Problem
#Given:
#numbers = [12, 45, 7, 89, 23]

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}")