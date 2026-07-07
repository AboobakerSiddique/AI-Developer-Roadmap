#for i in range(2):
  #  for j in range(3):
  #      print("#", end="")
  #  print()
  
print("---------Rectangle Generator-----------")
rows = int(input("No of rows: "))
columns = int(input("No of columns: "))

for i in range(rows):
    for j in range(columns):
        print('*', end='')
    print()