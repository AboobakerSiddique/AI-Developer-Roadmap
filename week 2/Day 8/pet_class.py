class Pet:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal

    def display_info(self):
        print(f"Name   : {self.name}")
        print(f"Animal : {self.animal}")


pets = []


def add_pet():
    pet_name = input("Enter pet name: ").strip()
    pet_animal = input("Enter animal type: ").strip()

    if pet_name == "" or pet_animal == "":
        print("Pet name and animal type cannot be empty.")
        return

    new_pet = Pet(pet_name.title(), pet_animal.title())
    pets.append(new_pet)

    print("Pet added successfully!")


def view_pets():
    if len(pets) == 0:
        print("\nNo pets added yet.")
        return

    print("\n-------- PET LIST --------")

    for index, pet in enumerate(pets, start=1):
        print(f"\nPet {index}")
        pet.display_info()

    print("--------------------------")


while True:
    print("\nPet Management System")
    print("------------------------")
    print("1. Add Pet")
    print("2. View Pets")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            add_pet()

        elif choice == 2:
            view_pets()

        elif choice == 3:
            print("Thanks for using Pet Management System!")
            break

        else:
            print("Please choose between 1 and 3.")

    except ValueError:
        print("Please enter numbers only.")