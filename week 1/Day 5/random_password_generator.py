import random
print("Random Password Generator")
print("-------------------------")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
password_length = int(input("Enter the desired password length: "))
try:
    if password_length < 1:
       print("Please enter a valid password length.")
    else:
       password=''
       for i in range(password_length):
            password += random.choice(characters)
    print(f"Your random password is: {password}")
except ValueError:
    print("Please enter numbers only.")
print("-------------------------")