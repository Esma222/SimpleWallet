class Wallet:
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Yetersiz Bakiye")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    