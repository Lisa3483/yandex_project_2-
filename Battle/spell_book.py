class Spell_book:
    def __init__(self):
        self.damage = 0

    def bolt(self, number_of_battle):
        self.damage = number_of_battle * 10 + 35

    def boom(self, number_of_battle):
        self.damage = 80
