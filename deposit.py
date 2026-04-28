from utils import balance, transactions

def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Deposited successfully")
    return balance
