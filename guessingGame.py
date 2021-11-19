import random
number = random.randint(1,9)
chances = 0

while chances < 5:
    guess = int(input("Guess a number between 1 and 9:- "))

    if (number == guess):
        print("You Win!!!")
        break
    elif (number < guess):
        print("You guess is too high, the number is lower than", guess)
    else:
        print("Your guess is too low, the number is higher than", guess)

    chances += 1

if not chances < 5:
   print("You lose! Better luck next time")