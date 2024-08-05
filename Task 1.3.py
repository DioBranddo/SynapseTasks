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
    }
}


def transactions(request_spending, account_id, category):
    return request_spending[account_id]["transactions"]["category"==category]["amount"]


def account_balance(request_spending, account_id):
    return request_spending[account_id]["balance"]


def money_owed(request_spending, account_id):
    return request_spending[account_id]["balance"] + sum(transaction["amount"]for transaction in request_spending[account_id]["transactions"])


print(money_owed(request_spending, "Mahek"))
