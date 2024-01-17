class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self._balance == other._balance
        return False

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Error: Balance cannot be negative.")

    @balance.deleter
    def balance(self):
        print("Deleting balance.")
        del self._balance

    def add_interest(self):
        self._balance += self._balance * self.interest_rate
        
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def subtract_fee(self):
        self._balance -= self.fee
# Create a CheckingAccount instance
checking_account = CheckingAccount(owner="John Doe", balance=1200, fee=15)

# Demonstrate methods and properties
checking_account.add_interest()
print(checking_account.balance)  # Display balance after interest

checking_account.subtract_fee()
print(checking_account.balance)  # Display balance after fee subtraction


# Use class method to change interest rate
BankAccount.set_interest_rate(0.07)

# Compare two CheckingAccount instances
checking_account_2 = CheckingAccount(owner="Jane Doe", balance=1200, fee=15)
print(checking_account == checking_account_2)  # True if balances are equal

# Represent an instance using __repr__
print(repr(checking_account))

# Implement decorator function to add a prefix to a method's result
def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix} {result}"
        return wrapper
    return decorator

# Apply the decorator to the description method
@add_prefix("Account Info:")
def account_info(account):
    return f"{account.owner} - Balance: {account.balance}"


# Display account info with the added prefix
print(account_info(checking_account))


