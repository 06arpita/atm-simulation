class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Checked balance")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited.")
            self.transaction_history.append(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn.")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient balance.")
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN successfully changed.")
            self.transaction_history.append("Changed PIN")
        else:
            print("Incorrect old PIN.")

    def show_transaction_history(self):
        if self.transaction_history:
            print("\nTransaction History:")
            for transaction in self.transaction_history:
                print(f" - {transaction}")
        else:
            print("No transactions yet.")

    def start(self):
        print("Welcome to the ATM!")
        entered_pin = input("Please enter your PIN: ")
        if entered_pin != self.pin:
            print("Incorrect PIN. Access denied.")
            return

        while True:
            print("\nPlease choose an option:")
            print("1. Account Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. PIN change")
            print("5. View Transaction History")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                self.change_pin(old_pin, new_pin)
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the ATM simulation
atm = ATM(balance=500)  # Initial balance can be set, and default PIN is '1234'
atm.start()
