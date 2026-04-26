from utils import load_accounts

def check_balance():
    accounts = load_accounts()

    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("Invalid account or PIN")