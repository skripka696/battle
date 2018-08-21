from random import random

from unit.unit import Unit


class Solid(Unit):
    """
    Soldiers are units that have an additional property:

    Property   | Range  | Description
    _______________________________________________________

    experience | [0-50] | Represents the soldier experience

    """
    def __init__(self, recharge, health, experience):
        self.recharge = recharge
        self.health = health
        self.experience = experience

    def attack(self):
        return 0.5*(1 + self.health/100)*random(50 + self.experience, 100) / 100

    def damage(self):
        """Сумма ущерба, нанесенного солдату, рассчитывается следующим образом:"""
        damage = 0.05 + self.experience / 100
        return self.calculate_damage(damage, self.health)

    def recalculate_health(self):
        damage = self.damage()
        self.health = self.health - damage
