from utils import transactions

def statement(transactions):
    print("\nTransactions:")
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        for t in transactions:
            print(t)
