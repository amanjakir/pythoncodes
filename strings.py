from pyexpat.errors import messages

# # course="python is program"
# course="program"
# # print(course.lower())
# # print(course.count("t"))
# # print(course.endswith("python"))
# # print(course.startswith("program"))
# print(course.partition('ro'))
#
# course=[1,3,5,7]
# sub=[6,8,11]
# course.append(10)
# course.extend(sub)
# a=["aman","jack","cherry"]
# a.insert(2,"tom")
# print(a)
#
# c=(0,1,2,3,4,5,6,4,5,4)
# c1=('python','for','jave','geek','geek')
#
# res =c.count(4)
# print('count of 4 in c is:',res)
#
# res =c1.count('geek')
# print('count of geek in c1 is:',res)
#
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
#
# res = Tuple.index(3)
# print('First occurrence of 3 is', res)
#
# res = Tuple.index(3, 4)
# print('First occurrence of 3 after 4th index is:', res)

# d = {1: "geeks", 2: "for"}
#
# d.clear()
# print(d)


original = {1: 'geeks', 2: 'for'}

new = original.copy()
new.clear()

print('new: ', new)
print('original: ', original)




new_dict = dict.fromkeys(range(4), [])

print("New dictionary with empty lists as keys : " + str(new_dict))