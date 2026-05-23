name = input("What is your name? ")

age = int(input("How old are you? "))

print("Welcome to Nexora,", name)

if age < 18:
    print("You are young")

elif age < 60:
    print("You are adult")

else:
    print("You are old")