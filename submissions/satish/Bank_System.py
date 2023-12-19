class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"

    def __eq__(self, other):
        return self._balance == other._balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    def add_interest(self):
        self._balance *= (1 + self.interest_rate)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def subtract_fee(self):
        self._balance -= self.fee


# Usage Examples
john_account = CheckingAccount("John Doe", 1200, 15)
john_account.subtract_fee()
john_account.add_interest()

# Additional Functionality
BankAccount.set_interest_rate(0.07)
mary_account = CheckingAccount("Mary Smith", 1500, 20)
print(john_account == mary_account)
print(repr(john_account))


# Decorator Function
def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}: {result}"

        return wrapper

    return decorator


@add_prefix("Result")
def example_method():
    return "This is a sample"


print(example_method())
