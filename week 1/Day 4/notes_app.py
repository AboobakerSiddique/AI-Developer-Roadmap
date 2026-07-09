import os

# Get the folder where this Python script is located
folder = os.path.dirname(__file__)

print("------------- Notes App -------------")

def add_note():
    note_name = input("Enter the note name: ")
    note_content = input("Enter the note content: ")

    with open(note_name + ".txt", "a") as file:
        file.write(note_content + "\n")

    print("✅ Note added successfully!\n")


def view_notes():
    note_name = input("Enter the note name to view: ")

    with open(note_name + ".txt", "r") as file:
        print("\n--------", note_name.title(), "--------")
        print(file.read())
        print("------------------------------------\n")


while True:

    print("------------------------------------")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Exit")
    print("------------------------------------")

    option = input("Enter your choice (1/2/3): ")

    if option == "1":
        add_note()

    elif option == "2":
        view_notes()

    elif option == "3":
        print("Thank you for using Notes App!")
        break

    else:
        print("❌ Invalid option. Please try again.\n")
        
        
    
