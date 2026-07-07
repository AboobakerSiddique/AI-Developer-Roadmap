print("---------Number Guessing Game-----------")
secret_number = 7
guess=int(input("Guess the secret number between 1 and 10: "))
while guess != 7:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the secret number between 1 and 10: "))
    print("Congratulations! You guessed the secret number.")