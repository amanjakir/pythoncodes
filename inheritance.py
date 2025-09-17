# class Animal:
#     def sound(self):
#         print("This animal make a sound.")
#
# class Dog(Animal):
#     def bark(self):
#         print("the dog barks: Woof! Woof!")
#
# d=Dog()
# d.sound()
# d.bark()





# Hierarchical Inheritance

# Base class
# class Parent:
#     def __init__(self):
#         print("Parent: called")
#
# # First derived class
# class Child1(Parent):
#     def __init__(self):
#         super().__init__()  # Call Parent's __init__
#         print("Child1:  called")
#
# # Second derived class
# class Child2(Parent):
#     def __init__(self):
#         super().__init__()  # Call Parent's __init__
#         print("Child2:  called")
#
# # Create objects
# print("Creating Child1 object:")
# c1 = Child1()
#
# print("\nCreating Child2 object:")
# c2 = Child2()

# #
# class Person:
#     def __init__(self):
#         print("person")
#
# class Father(Person):
#     def __init__(self):
#         super().__init__()
#         print("Father")
#
# class Mother(Person):
#     def __init__(self):
#         super().__init__()
#         print("Person")
#
# class Child(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         print("father and mother")
# print("Create child class")
#
# c1=Child()


class A:
    def __init__(self):
        print("Init of Class A")

class B(A):  # Inherits from A
    def __init__(self):
        super().__init__()
        print("Init of Class B")

class C:
    def __init__(self):
        print("Init of Class C")

class D(B,C):  # Inherits from both B and C
    def __init__(self):
        super().__init__()  # This follows MRO
        C.__init__(self)
        print("Init of Class D")

# Create an object of class D
obj = D()
