from sections import *


def handle_choice(choice):

    if choice == "1":
        welcome()

    elif choice == "2":
        print("HELP SECTION")

    elif choice == "3":
        print("ABOUT SECTION")

    elif choice == "4":
        print("SETTINGS SECTION")

    elif choice == "5":
        print("GOODBYE")
        return False

    else:
        print("Invalid choice")

    return True


while True:

    print("\n=== NEXORA MENU ===")
    print("1 - Start")
    print("2 - Help")
    print("3 - About")
    print("4 - Settings")
    print("5 - Exit")

    choice = input("Choose: ")

    result = handle_choice(choice)

    if result == False:
        break