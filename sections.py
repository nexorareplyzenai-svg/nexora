def separator():

    print("\n" + "=" * 35 + "\n")


def loading():

    print("Loading Nexora...")


def welcome():

    separator()

    print("WELCOME TO NEXORA")

    separator()

    name = input("What is your name? ")

    while True:

        age = input("How old are you? ")

        if age.isdigit():

            age = int(age)

            break

        else:

            print("Please enter a number")

    separator()

    print("Welcome to Nexora,", name)

    separator()


def help_section():

    print("HELP SECTION")


def about_section():

    print("ABOUT NEXORA")


def settings_section():

    print("SETTINGS")


def goodbye():

    print("Thank you for using Nexora")


def show_message(message):

    print(message)