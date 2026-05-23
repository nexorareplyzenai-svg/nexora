def welcome():

    name = input("What is your name? ")

    while True:

        try:
            age = int(input("How old are you? "))
            break

        except:
            print("Please enter a number")

    print("Welcome to Nexora,", name)

    if age < 18:
        print("You are young")

    elif age < 60:
        print("You are adult")

    else:
        print("You are old")


while True:
    welcome()