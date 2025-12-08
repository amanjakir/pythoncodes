class Laptops():
    def Specs(self,m,n):
        self.model=m
        self.Ram=n

    def Fun(self):
        print("hi")

ob1=Laptops()
ob2=Laptops()

ob1.Specs("hp","8GB")
print(ob1.model)
ob2.Specs("Lenovo","8GB")
print(ob2.model)











import re

bus_train_ticket_system=[]
seats_no= set()
users_data ={}
# E-mail verfication fon registration
# E-mail validation
#--------Registration User--------------
def register():
    print("--Create Account--")
    while True:
        pattern = r"[a-z0-9]=@[a-zA-Z]=\.(com)$"
        email=input("Set email:")
        if re.fullmatch(pattern,email):
            break
        else:
            print("invalid email format! please try again. ")

        while True:
            password=input("Set paasword:")
            if len(password)<4:
                print("invalid password (too short,must be atleast 4 character)")
            elif password.isdigit():
                print("Invalid password (cannot be only numbers")
            elif password.isalpha():
                print("Invalid password (cannot be only letters)")
            else:
                break
        print("Registration Successfulll....\n ")
        return {"email":email,"password":password}
def login(user):
    print("=== Sign In ===")
    for _ in range(3):
        entered_email = input("Enter email: ")
        entered_pass = input("Enter password: ")
        if entered_email == user.get("email") and entered_pass == user.get("password"):
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials, try again.")
    print("Too many failed attempts. Exiting...")
    users_data()   # Auto-save on failed login
    return False

#---------logout-------
def logout():
    print("signing out....")
    users_data()
    return False

#--------change emsil-------
def change_email(user_dict):
    while True:
        new_email = input("Enter new email: ")
        pattern = r"[a-z0-9]=@[a-zA-Z]=\.(com)$"
        if re.fullmatch(pattern, new_email):
            user_dict["email"] = new_email
            print("Email changed successfully!")
            users_data()
            break
        else:
            print("Invalid email format! Try again.")

#----------change password---------
def change_password(user_dict):
    while True:
        new_pass = input("Enter new password: ")
        if len(new_pass) < 4:
            print("Invalid password (too short, must be at least 4 characters)")
        elif new_pass.isdigit():
            print("Invalid password (cannot be only numbers)")
        elif new_pass.isalpha():
            print("Invalid password (cannot be only letters)")
        else:
            user_dict["password"] = new_pass
            print("Password changed successfully!")
            users_data()
            break

def add_passenger():
    try:
        while True:
            name=input("Enter passenger name:").strip().title()
            if not name:
                print("Name cannot be empty!")
            elif not all (ch.isalpha() or ch.isspace() for ch in name):
                 print("Name must contain only letter and space!")
            else:
                break

        seat_no=int(input("Enter seat no:"))
        if seat_no in seats_no:
            print("Seat number already exixts!")
            return

        tickets_price={}
        while True: