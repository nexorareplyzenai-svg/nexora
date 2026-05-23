def welcome():

    name = input("What is your name? ")

    while True:

        age = input("How old are you? ")

        if age.isdigit():
            age = int(age)
            break

        else:
            print("Please enter a number")

    print("Welcome to Nexora,", name)

    if age < 18:
        print("You are young")

    elif age < 60:
        print("You are adult")

    else:
        print("You are old")


def help_section():
    print("This is the help section")


def about_section():
    print("Nexora Version 1.0")


def menu():

    while True:

        print("\n=== NEXORA MENU ===")
        print("1 - Start")
        print("2 - Help")
        print("3 - About")
        print("4 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            welcome()

        elif choice == "2":
            help_section()

        elif choice == "3":
            about_section()

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


menu()