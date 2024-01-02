class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance

    def add_interest(self):
        self._balance += self._balance * self.interest_rate

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"

    def __eq__(self, other):
        return self._balance == other._balance

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def subtract_fee(self):
        self._balance -= self.fee


# Additional Functionality

def prefix_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix} {result}"
        return wrapper
    return decorator


# Usage Examples
if __name__ == "__main__":
    # Create an instance of CheckingAccount
    checking_acc = CheckingAccount(owner="John Doe", balance=1200, fee=15)

    # Demonstrate methods and properties
    print(f"current balance :   {checking_acc.balance}")  # Access balance using property
    checking_acc.subtract_fee() 
    print(f"fee reduction balance:  {checking_acc.balance}")  # Updated balance after subtracting fee

    # Demonstrate BankAccount methods
    checking_acc.add_interest()  # Add interest using the parent method
    print(f"balance with interest:  {checking_acc.balance}")  # Updated balance after adding interest

    # Use class method to change interest rate
    BankAccount.set_interest_rate(0.03)
    checking_acc.add_interest()  # Add interest with the updated interest rate
    print(f"balance based on updated interest: {checking_acc.balance}")  # Updated balance after adding interest with new rate

    # Compare two instances using the __eq__ method
    another_checking_acc = CheckingAccount(owner="kelvin", balance=1800, fee=20)
    if checking_acc == another_checking_acc:
        print('true based on matching balance amount')
    else:
        print('false based on not matching balance amount')    
    #print(checking_acc == another_checking_acc)  # True if balances are equal

    # Represent an instance using the __repr__ method
    print(repr(checking_acc))

    # Use the decorator function to add a prefix to a method's result
    #@prefix_decorator("Result:")
    def example_method():
        return "This is the result"

    print(example_method())  # Output: "Result: This is the result."
    