print("--------Multiplication Generator---------")
number=int(input("which number multiplication table: "))
print("Here is your multiplication table: ")
for multiplication in range(1,11):
    print(f"{number} * {multiplication} =",number*multiplication)