from quote_api import get_random_quote


def menu():
    while True:
        print("\n" + "=" * 40)
        print("      RANDOM QUOTE GENERATOR")
        print("=" * 40)
        print("1. Get Random Quote")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            quote, author = get_random_quote()

            if quote:
                print("\n" + "-" * 60)
                print(f'"{quote}"')
                print(f"\n— {author}")
                print("-" * 60)

        elif choice == "2":
            print("\nThank you for using Quote Generator!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()