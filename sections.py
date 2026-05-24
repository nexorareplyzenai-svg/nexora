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


def show_message(message):

    print(message)


def separator():

    print("\n" + "=" * 30 + "\n")


def loading():

    print("Loading Nexora...")


def goodbye():

    print("Thank you for using Nexora")