from utils import balance, transactions

def withdraw(balance):
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Withdraw successful")
    else:
        print("Not enough balance")
    return balance
