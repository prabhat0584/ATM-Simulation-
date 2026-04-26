from utils import load_accounts, save_accounts

def deposit():
    accounts = load_accounts()

    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        amount = int(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        save_accounts(accounts)
        print("Deposit successful!")
    else:
        print("Invalid account or PIN")