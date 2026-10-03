import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Let's choose a number between 1 and 100")

while True :
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < number :
        print("Too low! Try again.")
    elif guess > number :
        print("Too high! Try again.")
    else :
        print("🎉 Correct!")
        print("You gussed the number in", attempts,"attempts.")
        break