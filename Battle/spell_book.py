class Spell_book:
    def __init__(self):
        self.damage = 0

    def bolt(self, number_of_battle):
        self.damage = number_of_battle * 65 + 35
        return self.damage

    def boom(self, number_of_battle):
        self.damage = 200
        return self.damage
