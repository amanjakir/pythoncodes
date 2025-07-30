          # if condition: statements
# age=int(input("enter your age:"))
# if age>=18:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

# num=int(input("enter a number : "))
# if num % 2 == 0:
#     print(f"{num} is even number .")
# else:
#     print(f"{num} is odd number .")


# num=input("enter number separated by spaces :")
# number_list = list(map(int,num.split()))
# print("odd number")
# for num in number_list:
#     if num % 2==0:
#         print(num)

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# if a>b and b<a:
#     sum=a+b
#     print(a,"+",b,"=",sum)
# else:
#     print("enter a number is greater than 0")

# num1,num2=45,-12
# if num1>=0 and num2 >=0:
#     print(num1+num2)
# else:
#     print("please enter postive number" )

# y = 1904
# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# n
# elif num==1:
# print("Number is 1")
# elif num==2:
#    print("Number is 2")
# elif num==3:
#     print("Number is 3")
#     else:
#           print("Invalid choice")
# print("1.Addition\n2.Substraction\n3.Multiply\n4.division")
# choice=int(input("enter your choice:"))
# a=int(input("enter first number"))
# b=int(input("enter the second number"))
# if choice ==1:
#     print(a+b)
# elif choice==2:
#     print(a-b)
# elif choice==3:
#     print(a*b)
# elif choice==4:
#     print(a/b)
# else:
#     print("Invalid choice")
a=int(input("Enter first number"))
b=int(input("Enter the second number"))
print("1.Addition\n2.Substraction\n3.Multiply\n4.division")
choice=int(input("enter your choice:"))
match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case __:
        print("Invalid choice")
