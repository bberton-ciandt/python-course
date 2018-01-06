import random

highest = 1000
answer = random.randint(1, highest)

# original
# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

correct_answer = False
print("Please guess a number between 1 and {}: ".format(highest))
while not correct_answer:
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
        correct_answer = True
    elif guess == 0:
        print("Game Over")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
