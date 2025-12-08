# import re
#
# pattern ="hello"
# text="hello world"
# print(bool(re.search(pattern,text)))



''''''
# import re
# pattern=r"\d+"
# text="hel8lo worl89d"
# print(bool(re.search(pattern,text)))



import re

# pattern=r""
# text=""


# import re
# pattern=r"[a-z0-9]+@[a-zA-Z]+\.(com|in|org)"
# email=input("Enter the email:")
# if bool(re.match(pattern,email)):
#     print("valid email")
# else:
#     print("invalid email")



import re

password=input("Enter the password ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,16}$'
if bool(re.match(pattern,password)):
    print("valid password")
else:
    print("invalid password")




