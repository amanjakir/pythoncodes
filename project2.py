import random

class Bankaccount:
    total_accounts =0

    def __init__(self, name, acct_type, balance=0):
        self.name= name
        self.acct_type= acct_type
        self.balance= balance
        self.transactions= []
        self.acc_no= Bankaccount.generate_account_number()
        Bankaccount.total_accounts +=1

    def deposit(self,amount):
        self.balance+= amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f" Withdraw {amount}")
        else:
            self.transactions.append(f"Failed the withdrawal : 0 balance")

    def show_statement(self):
        print(f"\nStatement for {self.name} (Acc_no:{self.acc_no})")
        for txn in self.transactions:
            print("-",txn)
        print(f"Current Balance: {self.balance}")

    @staticmethod
    def generate_account_number():
        return f"ACC{random.randint(1000,9000)}"

    @classmethod
    def get_total_account(cls):
        return cls.total_accounts

    def __eq__(self, other):
        return self.acc_no == other.acc_no


account ={}

def to_create_account():
    name =input("Enter your name:")
    acct_type=input("Enter account type Saving/Current:")
    balance =float(input("Enter initial deposit:"))
    acc = Bankaccount(name,acct_type,balance)
    account[acc.acc_no]=acc
    print(f"Account created successfully! Your Account No is {acc.acc_no}")

def action():
    acc_no =input("Enter your Account number:")
    if acc_no not in account:
        print("Account not found.")
        return
    acc =account[acc_no]
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Show Statement\n4. Exit")
        choice =input("Choose an opition:")
        if choice == '1':
           amount = float(input("Enter amount to deposit:"))
           acc.deposit(amount)
        elif choice == '2':
            amount=float(input("Enter amount to withdraw:"))
            acc.withdraw(amount)
        elif choice == '3':
            acc.show_statement()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

to_create_account()
action()
print("Total Account Created:",Bankaccount.get_total_account())