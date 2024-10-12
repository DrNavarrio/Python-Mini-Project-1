import random

random_number = random.randrange(1,51)

while True:
    user_guess = input("Guess the number between 1 and 50 (or type 'quit' to stop playing).")

    if user_guess.lower() == 'quit':
        print("Thanks for playing, goodbye.")
        break

    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_guess < random_number:
        print("Too low! Try again")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break
