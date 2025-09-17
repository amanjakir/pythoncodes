# TASK-8

# Program to assign grade based on student's score

score = int(input("Enter the student's score (0–100): "))

if score > 95:
    print("Grade: A+")
    print(" Congratulations! High Distinction ")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")



''''''


# # Program to check if a number is positive, negative, or zero
#
# num = int(input("Enter a number: "))
#
# if num > 0:
#     print("The number is Positive.")
# elif num < 0:
#     print("The number is Negative.")
# else:
#     print("The number is Zero.")