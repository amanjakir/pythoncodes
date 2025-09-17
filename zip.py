l1=[52,"aman",23,8]
l2=["hi","ki",89]
s=list(zip(l1,l2))
# print(s)
for k,t in zip(l1,l2):
    print(k,t)
l1,l2=zip(*s)
print(l1)
print(l2)