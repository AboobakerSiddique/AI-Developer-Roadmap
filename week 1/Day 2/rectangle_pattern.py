4
print("---------Rectangle Generator-----------")
rows = int(input("No of rows: "))
columns = int(input("No of columns: "))

for i in range(rows):
    for j in range(columns):
        print('*', end='')
    print()