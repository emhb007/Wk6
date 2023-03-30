class Account:
    numCreated = 0

    def __init__(self, initial): # <-- 1000.00
        self._balance = initial  # _balance <-- 1000.00
        Account.numCreated += 1     # numCreated = 1

    def deposit(self, amt):
        self._balance += amt
        return

    def withdraw(self,amt):
        self._balance -= amt
        return

    def getbalance(self):
        return self._balance

    def add_interest():
        pass

    def __str__(self):
        return f"This would be an account id: ${self.getbalance()}"