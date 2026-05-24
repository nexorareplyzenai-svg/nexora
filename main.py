from sections import welcome
from sections import help_section
from sections import about_section
from sections import show_message
from sections import separator
from sections import loading
from sections import goodbye


def show_menu():

    print("\n=== NEXORA MENU ===")
    print("1 - Start")
    print("2 - Help")
    print("3 - About")
    print("4 - Exit")


def handle_choice(choice):

    loading()

    if choice == "1":
        welcome()

    elif choice == "2":
        help_section()

    elif choice == "3":
        about_section()

    elif choice == "4":
        goodbye()
        return False

    else:
        print("Invalid choice")

    show_message("Menu loaded successfully")

    return True


def main():

    running = True

    while running:

        show_menu()

        choice = input("Choose: ")

        separator()

        running = handle_choice(choice)


main()