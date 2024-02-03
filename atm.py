class ATM:
    def __init__(account):
        account.initial_balance = 10000
        account.transaction_fee = 0.75
        account.username_password = {
            "donyelqt": "donyelqt",
        }

    def check_initial_balance(account):
        print(f"Your current initial balance is: ${account.initial_balance}")

    def deposit(account, amount):
        account.initial_balance += amount
        account.initial_balance -= account.transaction_fee
        print(f"Total deposited amount: ${amount}. Your new initial balance is: ${account.initial_balance}")

    def withdraw(account, amount):
        amount = float(amount)
        account.initial_balance -= account.transaction_fee
        if amount < account.initial_balance:
            account.initial_balance -= amount
            print(f"Total withdrawn amount: ${amount}. Your new initial balance is: ${account.initial_balance}")
        else:
            print("Sorry your current balance is not enough.")

    def login(account):
        username = input("Please enter your username account: ")
        password = input("Enter your password to proceed: ")

        if username in account.username_password and account.username_password[username] == password:
            print("Login successful :))")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

def run_atm():
    atm = ATM()

    while True:
        if atm.login():
            break

    while True:
        print("\nChoose an option:")
        print("1. Check your initial balance")
        print("2. Deposit your money")
        print("3. Withdraw your money")
        print("4. Exit the atm machine")

        option = input("Please select a option number: ")

        if option == '1':
            atm.check_initial_balance()
        elif option == '2':
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
        elif option == '3':
            amount = float(input("Enter amount to withdraw: $"))
            atm.withdraw(amount)
        elif option == '4':
            print("Exiting the ATM machine program. Thank you for using my ATM machine program :))")
            break
        else:
            print("Invalid option number. Please try again.")

if __name__ == "__main__":
    run_atm()
