import random

secret_number = random.randint(1, 100)

max_attempts = 7
attempts = 0

print(" select a number between 1 and 100.")
print("You have", max_attempts, "attempts to guess it.")

while attempts < max_attempts:

    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < secret_number:
        print("Too low! Try again")

    elif guess > secret_number:
        print("Too high! Try again")

    else:
        print("Congratulations! You guessed it correctly!")
        print("Number of attempts:", attempts)
        break

else:
    print("\nSorry! You have used all your attempts")
    print("The correct number was:", secret_number)