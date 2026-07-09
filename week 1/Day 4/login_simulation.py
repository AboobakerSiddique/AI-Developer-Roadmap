print("         Login Simulation         ")
print("-------------------------------------")

username = "admin"
password = "password@123"
attempts = 3


def login():
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")

    if user_username == username and user_password == password:
        print("✅ Login successful!")
        return True
    
    elif user_username == username:
        print("❌ Invalid password.")
        return False
    
    else:
        print("❌ Invalid username or password.")
        return False


while attempts > 0:

    if login():
        break

    attempts -= 1
    print(f"Remaining attempts: {attempts}")

    if attempts == 0:
        print("🚫 Account Locked!!!!!!")