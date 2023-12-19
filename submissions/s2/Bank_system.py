class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance}, interest_rate={self.interest_rate})"

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self._balance == other._balance
        else:
            raise ValueError("You can compare only two BankAccount instances")

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance can't be negative")
        self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance

    def add_interest(self):
        self._balance += self._balance * self.interest_rate


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def __eq__(self, other):
        if isinstance(other, CheckingAccount):
            return self._balance == other._balance
        else:
            raise ValueError("You can compare only two CheckingAccount instances")

    def subtract_fee(self):
        self._balance -= self.fee


# Example usage
savings_account = BankAccount("Alice", 5000)
print(f"Savings Account: {savings_account}")
savings_account.add_interest()
print(f"Balance after interest: {savings_account.balance}")

BankAccount.set_interest_rate(0.1)
print(f"New Interest Rate: {BankAccount.interest_rate}")

online_account = CheckingAccount("Bob", 3000, 10)
print(f"Online Checking Account: {online_account}")
online_account.add_interest()
print(f"Balance after interest: {online_account.balance}")

online_account.subtract_fee()
print(f"Balance after fee deduction: {online_account.balance}")

savings_account_2 = BankAccount("Alice", 5000)
print(f"Savings Accounts are equal: {savings_account == savings_account_2}")

another_online_account = CheckingAccount("Bob", 3000, 10)
print(f"Checking Accounts are equal: {online_account == another_online_account}")

print(repr(online_account))
