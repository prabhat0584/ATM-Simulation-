from utils import load_accounts, save_accounts

def create_account():
    accounts = load_accounts()

    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Name: ")
    pin = input("Set PIN: ")

    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0
    }

    save_accounts(accounts)
    print("Account created successfully!")