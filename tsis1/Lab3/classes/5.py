class Account():
    owner = ""
    balance = 0

    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance

    def __str__(self):
        return f"The owner of this account is: {self.owner}\nCurrent account balance is: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return "Deposit!!"

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            return "Withdraw accepted"
        else:
            return "Withdraw can not be accepted"

test_account = Account("Ayazhan", 12500)
print(test_account)

print(test_account.deposit(500))
print(test_account.withdraw(2700))
print(test_account.balance)