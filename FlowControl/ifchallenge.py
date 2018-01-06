name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age <= 30:
    print("Welcome to the holiday {0}".format(name))
else:
    print("You are not welcome to the holiday {0}".format(name))
