print("            Login Simulation       ")
print("-------------------------------------")
username="admin"
password="password@123"
attempts = 3
def login():
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    if user_username == username and user_password == password:
        print("✅ Login successful!")
    else:
        print("❌ Invalid username or password. Please try again.")
        attempts -= 1
        print(f"Remaining attempts: {attempts}")
        
        

while attempts > 0:
    login()
    attempts -= 1
    if attempts == 0:
    print("Account Locked !!!!!!!")