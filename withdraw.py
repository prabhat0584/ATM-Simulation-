from utils import load_accounts, save_accounts

def withdraw():
    accounts = load_accounts()

    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        amount = int(input("Enter amount to withdraw: "))

        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            save_accounts(accounts)
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Invalid account or PIN")