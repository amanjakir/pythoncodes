# a,b=45,0
# try:
#     print(a/b)
# except Exception:
#     print("Error")
#
# a, b = 45,
# try:
#     print(a / b)
# except Exception as e:
#     print("Error",e)
#
#
# a, b = 45,4
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide by zero")
# except TypeError:
#     print("Please provide integer value")
# except NameError:
#     print("Value not provided for variable")
# except Exception as e:
#     print("Error")


g={"name":"aman"}
try:
    print(g['name'])
except KeyError:
    print("Key not found")