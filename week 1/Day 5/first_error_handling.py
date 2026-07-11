while True:
    try:
        number = int(input("Enter a number: "))
        print(number)
        break
    except:
        print("Please enter numbers only.")