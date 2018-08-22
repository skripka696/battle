import random
from datetime import datetime

from unit.unit import Unit


class Soldier(Unit):
    """
    Soldiers are units that have an additional property:

    Property   | Range  | Description
    _______________________________________________________

    experience | [0-50] | Represents the soldier experience

    """
    def __init__(self, health, name, attack_time=None, recharge=None):
        self.recharge = recharge
        self.health = health
        self.experience = 0
        self.attack_time = attack_time
        self.name = name
        self.type = 'Soldier'

    def attack(self):
        return 0.5 * (1 + self.health/100) * random.randint(50 + self.experience, 100) / 100

    def damage(self):
        damage = 0.05 + self.experience / 100
        return damage

    @property
    def is_alive(self):
        return self.health > 0

    @property
    def check_recharge(self):
        if self.attack_time:
            time_delta = self.attack_time - datetime.now()
            if time_delta.microseconds >= self.recharge:
                return True
            else:
                return False
        else:
            return True

    def recalculate_health(self):
        damage = self.damage()
        self.health = self.health - damage
