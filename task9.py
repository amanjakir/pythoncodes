# TASK-9
#  Sum of Numbers

total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)



# Filter Even Numbers

numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)


#  Multiplication Table (1 to 5)

print("\nMultiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}", end="  ")  # formatted for neat spacing
    print()
