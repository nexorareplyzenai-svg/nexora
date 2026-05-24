def separator():

    print("\n" + "=" * 30 + "\n")


def title(text):

    separator()

    print(text)

    separator()


def show_message(message):

    print(message)


def loading():

    print("Loading Nexora...")


def goodbye():

    print("Thank you for using Nexora")


def help_section():

    title("HELP SECTION")

    print("This is the help section")


def about_section():

    title("ABOUT NEXORA")

    print("Nexora Version 1.0")


def welcome():

    title("WELCOME TO NEXORA")

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

    if age < 18:
        print("You are young")

    elif age < 60:
        print("You are adult")

    else:
        print("You are old")

    separator()