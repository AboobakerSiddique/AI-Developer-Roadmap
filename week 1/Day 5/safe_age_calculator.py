print("        Safe Age Calculator        ")
print("-------------------------------------")
while True:
    
    current_year = 2026
    try:
        birth_year = int(input("\nEnter your birth year: "))
        if 1900 < birth_year < current_year:
            age = current_year - birth_year
            print(f"You are {age} years old.")
            break
        else:
            print("Please enter a valid year.")
    except ValueError:
        print("Please enter numbers only.")
    finally:
        print("Thank you for using the Safe Age Calculator.")
        print("-------------------------------------")
