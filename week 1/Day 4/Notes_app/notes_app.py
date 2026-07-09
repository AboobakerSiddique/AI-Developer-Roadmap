import os
folder = os.path.dirname(os.path.abspath(__file__))
print("Folder path:", folder)
print("------------- Notes App -------------")


def add_note():
    note_name = input("Enter the note name: ")
    note_content = input("Enter the note content: ")

    # Create the complete file path
    filepath = os.path.join(folder, note_name + ".txt")

    with open(filepath, "a") as file:
        file.write(note_content + "\n")

    print("✅ Note added successfully!\n")


def view_notes():
    note_name = input("Enter the note name to view: ")

    # Create the complete file path
    filepath = os.path.join(folder, note_name + ".txt")

    with open(filepath, "r") as file:
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