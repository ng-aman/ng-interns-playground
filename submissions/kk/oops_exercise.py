class BankAccount:
    intrest_rate = 0.05

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance_ = balance

    def __repr__(self):
        return f"Account('owner name :'{self.owner}, balance : {self.balance_})"
    
    def __eq__(self, other) :
        if isinstance(other, BankAccount):
            return self.balance_ == other.balance_
        return False
    
    @classmethod
    def set_interest_rate(cls, rate):
        cls.intrest_rate = rate
    
    @property
    def balance(self):
        return self.balance_
    
    
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.balance_ = new_balance
        else:
            print("Error: Balance cannot be negative.")
        

    @balance.deleter
    def balance(self):
        print('deleting balance ')
        del self.balance_

    def add_interest(self):
        self.balance_ += self.balance_*self.intrest_rate

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def subtract_fee(self):
        self.balance_ = self.balance_-self.fee


checking_acount_1 = CheckingAccount('John Doe',1200, 15)

print(checking_acount_1.__repr__())
print(f'initial balane {checking_acount_1.balance}')
checking_acount_1.add_interest()
print(f'balance after added intrest {checking_acount_1.balance}')
print(checking_acount_1.subtract_fee())
print(f'balance after subtracting fee {checking_acount_1.balance}')
print(checking_acount_1.__repr__())

# for intrest rate of o.o2
print('***********************')
print('intrest rate changed to 0.02')
checking_acount_1 = CheckingAccount('John Doe',1200, 15)
checking_acount_1.set_interest_rate(0.02)
print(checking_acount_1.__repr__())
print(f'initial balane {checking_acount_1.balance}')
checking_acount_1.add_interest()
print(f'balance after added intrest {checking_acount_1.balance}')
print(checking_acount_1.subtract_fee())
print(f'balance after subtracting fee {checking_acount_1.balance}')
print(checking_acount_1.__repr__())

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
print(account_info(checking_acount_1))

