from show_balance import show_balance
from deposit import deposit
from withdraw import withdraw
from utils import balance, transactions
from statement import statement

while True:
    print("\n1. Balance  2. Deposit  3. Withdraw  4. Statement  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_balance(balance)

    elif choice == "2":
        balance = deposit(balance)
        transactions.append("Deposited money")

    elif choice == "3":
        balance = withdraw(balance)
        transactions.append("Withdrawn money")

    elif choice == "4":
        statement(transactions)

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Wrong choice")