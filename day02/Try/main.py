import sys
from my_app import get_current_weather, pretty_print_weather


def main_menu():
    print("\n=== MAIN MENU ===")
    print("1. Weather App")
    print("2. Exit")


def weather_driver():
    city = input("\nEnter city: ")
    try:
        data = get_current_weather(city)
        pretty_print_weather(data)
    except Exception as e:
        print("Error:", e)


def main():
    while True:
        main_menu()
        choice = input("Choice: ")
        if choice == "1":
            weather_driver()
        elif choice == "2":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
