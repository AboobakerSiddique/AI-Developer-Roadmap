print("Dice Roller")
print("------------")
import random
while True:
    play_again = input("Do you want to roll a dice? (y/n): ").lower()
    if play_again == "n":
        print("Thank you for using the Dice Roller.")
        break
    elif choice != "y":
        print("Please enter 'y' or 'n'.")
        continue
    try:
        sides=int(input("Enter the number of sides on the dice: "))
        if sides < 1:
            print("Please enter a valid number of sides.")
            continue
        else:
            roll = random.randint(1, sides)
            print(f"You rolled a {roll}.")
            print("------------")
            
    except ValueError:
        print("Please enter numbers only.")
        