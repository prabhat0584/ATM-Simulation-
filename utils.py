def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                acc_no, name, pin, balance = line.strip().split(",")
                accounts[acc_no] = {
                    "name": name,
                    "pin": pin,
                    "balance": int(balance)
                }
    except FileNotFoundError:
        pass
    return accounts


def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for acc_no, details in accounts.items():
            line = f"{acc_no},{details['name']},{details['pin']},{details['balance']}\n"
            file.write(line)