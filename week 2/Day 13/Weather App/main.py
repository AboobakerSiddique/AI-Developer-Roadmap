from weather_api import get_weather


def display_weather(weather):
    print("\n" + "=" * 45)
    print("         CURRENT WEATHER")
    print("=" * 45)

    print(f"City        : {weather['city']}")
    print(f"Country     : {weather['country']}")
    print(f"Temperature : {weather['temperature']}°C")
    print(f"Feels Like  : {weather['feels_like']}°C")
    print(f"Humidity    : {weather['humidity']}%")
    print(f"Pressure    : {weather['pressure']} hPa")
    print(f"Wind Speed  : {weather['wind_speed']} m/s")
    print(f"Condition   : {weather['condition']}")

    print("=" * 45)


def menu():
    while True:
        print("\n===== WEATHER APP =====")
        print("1. Check Weather")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            city = input("Enter city name: ").strip()

            if not city:
                print("City name cannot be empty.")
                continue

            weather = get_weather(city)

            if weather:
                display_weather(weather)

        elif choice == "2":
            print("Thank you for using Weather App!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()