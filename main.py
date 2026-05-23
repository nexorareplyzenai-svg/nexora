from sections import welcome
from sections import help_section
from sections import about_section


def show_menu():

    print("\n=== NEXORA MENU ===")
    print("1 - Start")
    print("2 - Help")
    print("3 - About")
    print("4 - Exit")


def handle_choice(choice):

    if choice == "1":
        welcome()

    elif choice == "2":
        help_section()

    elif choice == "3":
        about_section()

    elif choice == "4":
        print("Goodbye")
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