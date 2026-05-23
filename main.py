def get_age():

    while True:

        try:
            age = int(input("How old are you? "))
            return age

        except:
            print("Please enter a number")


def welcome():

    name = input("What is your name? ")

    age = get_age()

    print("Welcome to Nexora,", name)

    if age < 18:
        print("You are young")

    elif age < 60:
        print("You are adult")

    else:
        print("You are old")


welcome()