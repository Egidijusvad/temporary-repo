import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Please enter your guess (or type 'quit' to exit): ")
    if guess.lower() == 'quit':
        print("Thank you for playing")
        break

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.")
        break
