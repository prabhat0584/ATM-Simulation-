from create_account import create_account
from deposit import deposit
from withdraw import withdraw
from balance import check_balance

def main():
    while True:
        print("\n ATM MENU ")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()