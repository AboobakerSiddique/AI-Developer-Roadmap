#Create empty dictionary
#Create add_contact()
#Ask for name
#Ask for phone
#Store in dictionary
#Call function 3 times
#Print dictionary

print("----------- Contact Book -----------")

contact_book = {}

def add_contact():
    name = input("Enter contact name: ".capitalize())
    phone = input("Enter phone number: ")

    contact_book[name] = phone
    print()

# Call the function 3 times
add_contact()
add_contact()
add_contact()

print("----------- Contact Book -----------")

for name, phone in contact_book.items():
    print(f"{name}: {phone}")

print("------------------------------------")