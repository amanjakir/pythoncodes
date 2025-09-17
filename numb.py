# def add(*args):
#     sum == 0
from function import is_prime

# num=(12,-6,87,8,-2)
# for k in num:
#     if k <=0:
#         print("negative")
#     else:
#         print("positive")





num=int(input("Enter the number"))
if num <=1:
    is_prime=True
for i in range(2,num+1):
    if i % 1==0:
        is_prime=False