#
# num=1
# while num<=5:
#     print(num,end=" ")
#     num+=1
from itertools import count

#
# count=1
# while count<=10:
#     print(count)
#     count+=1


# count = 1
# number=int(input("Enter the number:"))
# while count <=5:
#     if count==5:
#         continue
#     print(f"{count} * {number} = {count * number}")
#     count += 1


count =1
while count<=10:
    if count==5:
        count+=1
        continue
    print(count)
    count+=1