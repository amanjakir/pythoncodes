# Program to print a rectangle with 4 rows and 6 columns of stars

for i in range(4):
    for j in range(6):
        print("*", end=" ")
    print()


# Program to create a hollow square pattern

for i in range(5):             # Loop for rows
    for j in range(5):         # Loop for columns
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")   # Print star for borders
        else:
            print(" ", end=" ")   # Print space inside
    print()  # Move to next line


# Program to print a reverse number pyramid starting from 5

for i in range(5, 0, -1):        # Loop from 5 down to 1
    for j in range(1, i + 1):    # Print numbers from 1 to i
        print(j, end=" ")
    print()  # Move to next line
