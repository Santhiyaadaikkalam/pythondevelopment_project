class ATM:
    def __init__(self):
        self.balance = 0
        self.is_authenticated = False

    def authenticate(self):
        pin = "1234"  # For simplicity, we're using a hardcoded PIN
        attempt = input("Enter PIN: ")
        if attempt == pin:
            self.is_authenticated = True
            print("Authentication successful.")
        else:
            print("Incorrect PIN.")

    def check_balance(self):
        if not self.is_authenticated:
            print("Please authenticate first.")
            return
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self):
        if not self.is_authenticated:
            print("Please authenticate first.")
            return
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount:.2f}. New balance is: ${self.balance:.2f}")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def withdraw(self):
        if not self.is_authenticated:
            print("Please authenticate first.")
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrew ${amount:.2f}. New balance is: ${self.balance:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Authenticate")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.authenticate()
            elif choice == '2':
                self.check_balance()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
