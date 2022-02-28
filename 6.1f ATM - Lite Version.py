#6.1f ATM - Lite Version


class ATM:
    """
    Automatic Teller Machine class 
    """


    def __init__(self, balance):
        self.balance = balance
                
                
    def menu(self):
        print("""Welcome to Northern Frock
    1 - Display balance
    2 - Withdraw funds
    3 - Deposit funds
    9 - Return card""")
        self.option = input("Enter an option: ").strip()


    def display_balance(self):
        self.max_withdrawal = round(self.balance//10*10)
        return f"Current balance: £{self.balance}\nMaximum amount available for withdrawal: £{self.max_withdrawal}"


    def withdraw_funds(self):
        amount_numbers = (10, 20, 40, 60, 80, 100)
        amounts = [f"£{i}" for i in amount_numbers]
        try:
            choice = input(f"Select amount: {', '.join(amount for amount in amounts)} or 'other'\n").strip()
            if choice.lower() in ("other", "'other'", '"other"'):
                choice = float(input("Enter amount to withdraw. Must be a multiple of 10.\n").strip())
                return self.attempt_withdrawal(choice) if choice % 10 == 0 and choice > 0 else "Invalid input"                                   
            if choice.startswith("£") and len(choice) > 1:
                choice = choice[1:]
            choice = float(choice)         
            return self.attempt_withdrawal(choice) if choice in amount_numbers else "Invalid input"
        except ValueError:
            return "Invalid input"


    def attempt_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance = round(self.balance - amount, 2)
            return f"Money withdrawn successfully.\nNew balance: £{self.balance}"
        return "Insufficient funds"         


    def deposit_funds(self):
        amount = float(input("Deposite amount:\n£"))
        if amount > 0:
            self.balance = round(self.balance + amount, 2)
            return f"Money deposited successfully.\nNew balance: £{self.balance}"
        return "Invalid input"
            


    


if __name__ == "__main__":
    atm = ATM(67.14)
    while True:
        atm.menu()
        commands = {
            "1": lambda: print(atm.display_balance()),
            "2": lambda: print(atm.withdraw_funds()),
            "3": lambda: print(atm.deposit_funds()),
            "9": lambda: print("Goodbye!"),
        }
        commands.get(atm.option, lambda: print("Invalid input"))()
        if atm.option == "9":
            break 
        print("\n")

              
              
              

    
