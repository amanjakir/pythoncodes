# task-13
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))


""""""
# Lambda function
square = lambda a: a * a
print(square(7))
