print("-----------Password Checker-----------")
password = ("harishbasheer@123")
user_password = input("Enter your password: ")

attempts = 3
while attempts > 0:
    if user_password == password:
        print("Password is correct!\nAccess granted.")
        break
    else:
        print("Password is incorrect!\nattempts left:", attempts - 1)
        attempts -= 1
        if attempts > 0:
            user_password = input("Enter your password: ")
else:
    print("Too many incorrect attempts.")