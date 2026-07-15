#Problem 2 – Count Even Numbers ⭐⭐
#Given:
#numbers = [10, 15, 22, 7, 8, 13, 40]

numbers = [10, 15, 22, 7, 8, 13, 40]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
           
print(count)        