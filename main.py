from sections import *

def show_menu():

    separator()

    print("=== NEXORA MENU ===")

    separator()

    print("1 - Start")
    print("2 - Help")
    print("3 - About")
    print("4 - Settings")
    print("5 - Exit")

    separator()


def handle_choice(choice):

    if choice == "1":

        loading()

        welcome()

    elif choice == "2":

        help_section()

    elif choice == "3":

        about_section()

    elif choice == "4":

        settings_section()

    elif choice == "5":

        loading()

        goodbye()

        return False

    else:

        print("Invalid choice")

    return True


def main():

    running = True

    while running:

        show_menu()

        choice = input("Choose: ")

        running = handle_choice(choice)


main()