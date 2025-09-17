# TASK-10
#  Password Validation

password = ""
while password != "python123":
    password = input("Enter password: ")
else:
    print("Correct password!")



#Find a Number

numbers = [1, 2, 3, 4, 5]
target = 5

for num in numbers:
    if num == target:
        print("Number found!")
        break
else:
    print("Number not found!")






#  Simple Guessing Game

secret = 7
guess = None

while guess != secret:
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print(" Correct You guessed the secret number.")
        break
else:
    # This will only run if the loop finishes without 'break'
    print("You failed to guess the number.")
