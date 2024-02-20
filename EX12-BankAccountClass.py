# Bank Account Class

# Develop a BankAccount class with the attributes balance and limit. 
# The getter and setter methods should ensure that the balance and limit are not set as negative values. 
# Additionally, add methods for deposit and withdrawal that respect the account limit.

class BankAccount:
    def __init__(self, balance: float, limit: float):
        self._balance = max(0, balance)  # Ensure non-negative balance
        self._limit = max(0, limit)  # Ensure non-negative limit

    # Getter methods
    def get_balance(self) -> float:
        return self._balance

    def get_limit(self) -> float:
        return self._limit

    # Setter methods
    def set_balance(self, new_balance: float) -> None:
        if new_balance >= 0:
            self._balance = new_balance

    def set_limit(self, new_limit: float) -> None:
        if new_limit >= 0:
            self._limit = new_limit

    # Deposit method
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount

    # Withdrawal method
    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance + self._limit:
            self._balance -= amount
        else:
            print("Insufficient funds or exceeding account limit.")

# Example usage
account = BankAccount(balance=1000, limit=500)
print(f"Initial balance: {account.get_balance():.2f}€")
account.deposit(300)
print(f"Balance after deposit: {account.get_balance():.2f}€")
account.withdraw(800)
print(f"Balance after withdrawal: {account.get_balance():.2f}€")
