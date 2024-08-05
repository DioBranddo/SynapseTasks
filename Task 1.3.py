request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham": {
        "balance": 5000.00,
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "Unnati": {
        "balance": 3500.00,
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang": {
        "balance": 2000.00,
        "transactions": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}


def total_spending(request_spending, account_id, category):
    return sum(transaction['amount'] for transaction in request_spending[account_id]["transactions"] if transaction['category'] == category)


def account_balance(request_spending, account_id):
    return request_spending[account_id]["balance"]


def money_owed(request_spending, account_id):
    return request_spending[account_id]["balance"] + sum(transaction["amount"]for transaction in request_spending[account_id]["transactions"])


def main():
    while(choice := input("Enter your choice:\n\t1.Check Total Spending\n\t2.Check Account Balances\n\t3.Check Money Owed\n\n")) not in {'1', '2', '3'}:
        print("Invalid choice, please enter 1, 2, or 3.")

    choice = int(choice)
    
    if choice == 1:
        account_id = input('Enter the name : ')
        category = input('Enter category : ')
        print( "Total Spending = ", total_spending(request_spending, account_id, category))
    elif choice == 2:
        account_id = input('Enter the name : ')
        print("Account Balance = ", account_balance(request_spending, account_id))
    else:
        account_id = input('Enter the name : ')
        print("Money owed = ", money_owed(request_spending, account_id))
if __name__ == '__main__':
    main()