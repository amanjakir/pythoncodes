# def Greetings(name,age):
#     print("hello",name,"you are",age,"years old")
# Greetings("jack",32)
#
# def is_even(num1):
#     if num1%2==0:
#         print(num1,"is even")
#     else:
#         print(num1,"is odd")
# num1=int(input("Enter the number :"))
# is_even(num1)

# def Addition(x=+,y=12):
#     print(x+y)
# a=15
# b=10
# Addition(a)
# Addition(a,b)

# def Factorial(num):
#     fact =1
#     for n in range(1, num + 1):
#         fact = fact * n
#     print(f"Factorial of {num} is {fact}")
# num=int(input("Enter the number :"))
# Factorial(num)




num = int(input("Enter a number: "))
if num <= 1:

    is_prime = True
    for i in range(2, num  + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


# num = int(input("Enter a number: "))
# if num <=1:
#     is_prime= True
#     for i in range(2, num ** 0.5 ):
#         if num % i == 0:
#            is_prime = False
#            break
#     if is_prime:
#         print("prime number")
#     else:
#         print("not a prime number")


# def Addition(a,b):
#     print("hi")
#     return a+b
#
#
# s=Addition(67,33)
# print("Sum is ",s)

def f():
    print(a)
a="hello"
f()
print(a)







