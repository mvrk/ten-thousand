
class Banker:

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amount_total):
        self.shelved += amount_total

    def clear_shelf(self):
        self.shelved = 0


