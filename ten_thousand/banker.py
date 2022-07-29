class Banker:
    def __init__(self):
        self.shelved = 0
        self.total = 0

    def shelf(self, unbanked_points):
        self.shelved += unbanked_points

    def bank(self):
        self.total+= self.shelved
        self.shelved = 0
        return self.total

    def clear_self(self):
        self.shelved = 0


