import re
import json

bus_train_ticket_system = []
seats_no = set()
users_data = {}

DATA_FILE = "data.txt"

# -------- Save & Load Helpers --------------
def save_data():
    with open(DATA_FILE, "w") as f:
        for p in bus_train_ticket_system:
            line = f"{p['name']}|{p['seat_no']}|{p['ticket_type']}|{p['ticket_price']}|\n"
            f.write(line)


def load_data():
    global bus_train_ticket_system, seats_no
    bus_train_ticket_system = []
    seats_no = set()
    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.strip():  # skip empty lines
                    parts = line.strip().split('|')
                    if len(parts) >= 4:
                        name, seat_no, ticket_type, ticket_price = parts[:4]
                        seat_no = int(seat_no)
                        ticket_price = int(ticket_price)
                        seats_no.add(seat_no)
                        bus_train_ticket_system.append({
                            "name": name,
                            "seat_no": seat_no,
                            "ticket_type": ticket_type,
                            "ticket_price": ticket_price
                        })
    except FileNotFoundError:
        bus_train_ticket_system, seats_no = [], set()



# -------- Registration User --------------
def register():
    print("--Create Account--")
    while True:
        pattern = r"[a-z0-9]+@[a-zA-Z]+\.(com)$"
        email = input("Set email: ")
        if re.fullmatch(pattern, email):
            break
        else:
            print("Invalid email format! Please try again.")

    while True:
        password = input("Set password: ")
        if len(password) < 4:
            print("Invalid password (too short, must be at least 4 characters)")
        elif password.isdigit():
            print("Invalid password (cannot be only numbers)")
        elif password.isalpha():
            print("Invalid password (cannot be only letters)")
        else:
            break

    print("Registration Successful!\n")
    return {"email": email, "password": password}

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
    return False

# -------- Logout -------
def logout():
    print("Signing out....")
    return False

# -------- Change email -------
def change_email(user_dict):
    while True:
        new_email = input("Enter new email: ")
        pattern = r"[a-z0-9]+@[a-zA-Z]+\.(com)$"
        if re.fullmatch(pattern, new_email):
            user_dict["email"] = new_email
            save_data()  # Save after email change
            print("Email changed successfully!")
            break
        else:
            print("Invalid email format! Try again.")

# ---------- Change password ---------
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
            save_data()  # Save after password change
            print("Password changed successfully!")
            break

# -------- Add passenger --------
def add_passenger():
    try:
        # ---- Passenger Name ----
        while True:
            name = input("Enter passenger name: ").strip().title()
            if not name:
                print("Name cannot be empty!")
            elif not all(ch.isalpha() or ch.isspace() for ch in name):
                print("Name must contain only letters and spaces!")
            else:
                break

        # ---- Seat Number (auto-assigned) ----
        seat_no = 1
        while seat_no in seats_no:
            seat_no += 1
        seats_no.add(seat_no)
        print(f"Assigned Seat Number: {seat_no}")

        # ---- Ticket Price ----
        print("\n--- Ticket Options ---")
        print("1. Bus - ₹100")
        print("2. Train - ₹200")

        while True:
            choice = input("Choose ticket type (1/2): ").strip()
            if choice == "1":
                ticket_type = "Bus"
                ticket_price = 100
                break
            elif choice == "2":
                ticket_type = "Train"
                ticket_price = 200
                break
            else:
                print("Invalid choice! Please select 1 or 2.")

        # ---- Save Passenger Data ----
        passenger = {
            "name": name,
            "seat_no": seat_no,
            "ticket_type": ticket_type,
            "ticket_price": ticket_price
        }
        bus_train_ticket_system.append(passenger)
        save_data()  # Save after adding passenger

        print(f"\nPassenger added successfully: {passenger}\n")

    except ValueError:
        print("Invalid input! Seat number must be a number.")

# -------- View all tickets --------
def view_tickets():
    if not bus_train_ticket_system:
        print("No tickets booked yet.")
        return
    print("\n--- All Booked Tickets ---")
    for idx, p in enumerate(bus_train_ticket_system, start=1):
        print(f"{idx}. Name: {p['name']} | Seat: {p['seat_no']} | {p['ticket_type']} | Price: ₹{p['ticket_price']}")
    print()

# -------- Cancel ticket --------
def cancel_ticket():
    if not bus_train_ticket_system:
        print("No tickets to cancel.")
        return
    view_tickets()
    try:
        num = int(input("Enter ticket number to cancel: "))
        if 1 <= num <= len(bus_train_ticket_system):
            removed = bus_train_ticket_system.pop(num - 1)
            seats_no.remove(removed['seat_no'])
            save_data()  # Save after cancellation
            print(f" Ticket for {removed['name']} (Seat {removed['seat_no']}) cancelled.")
        else:
            print("Invalid ticket number.")
    except ValueError:
        print("Invalid input! Must be a number.")

# -------- Booking Menu --------
def booking_menu(user):
    while True:
        print("\n--- Ticket Booking System ---")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View Tickets")
        print("4. Change Email")
        print("5. Change Password")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_passenger()
        elif choice == "2":
            cancel_ticket()
        elif choice == "3":
            view_tickets()
        elif choice == "4":
            change_email(user)
        elif choice == "5":
            change_password(user)
        elif choice == "6":
            logout()
            break
        else:
            print("Invalid choice!")

# -------- Main Program --------
if __name__ == "__main__":
    load_data()  # Load data from file at start
    print("=== Welcome to Bus & Train Ticket System ===")
    user = register()
    users_data[user["email"]] = user  # Save new user
    save_data()  # Save after registration
    if login(user):
        booking_menu(user)
