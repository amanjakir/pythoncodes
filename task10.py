# TASK-10
# Exercise 3: Simple Guessing Game

secret = 7
guess = None

while guess != secret:
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print("🎉 Correct! You guessed the secret number.")
        break
else:
    # This will only run if the loop finishes without 'break'
    print("You failed to guess the number.")
