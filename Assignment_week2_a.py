
import random
num_guess = 7
num = random.randint(1,1000)
guess = 0

while guess != num:
    guess = int(input("Enter guess:"))
    num_guess = 1
    if guess < num:
        print("Too low,guess higher")
    elif guess > num:
        print("Too high,guess lower")
    elif num_guess == 1:
        print("Try again")
    else:
        print("You won!!!")


