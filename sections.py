def separator():
    print("=" * 35)


def help_section():
    separator()

    print("HELP SECTION")

    separator()

    print("1 - Start the program")
    print("2 - Open help")
    print("3 - About Nexora")
    print("4 - Settings")
    print("5 - Exit")

    separator()


def about_section():
    separator()

    print("ABOUT NEXORA")

    separator()

    print("Nexora Version 1.0")
    print("Built with Python")
    print("Console Application Project")

    separator()


def settings_section():
    separator()

    print("SETTINGS SECTION")

    separator()

    print("Theme: Default")
    print("Language: English")
    print("Mode: Console")

    separator()


def loading():
    separator()

    print("Loading Nexora...")

    separator()


def welcome():
    separator()

    print("WELCOME TO NEXORA")

    separator()

    name = input("What is your name? ")

    age = input("How old are you? ")

    separator()

    print(f"Welcome to Nexora, {name}")

    if int(age) < 18:
        print("You are young")

    else:
        print("You are old")

    separator()