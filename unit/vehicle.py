import random

from datetime import datetime
from unit.unit import Unit, SubUnit

from unit.solider import Soldier
from utils import count_gavg, set_soldier_name


class Vehicle(Unit, SubUnit):
    """
    battle vehicle has these additional properties:

    Property  | Range | Description
    __________________________________________________________________________

    operators | [1-3] | The number of soldiers required to operate the vehicle
    """
    def __init__(self,  health, name, operators, recharge=None, attack_time=None):
        self.name = name
        self.health = health
        self.recharge = recharge
        self.operators_count = operators
        self.attack_time = attack_time
        self.operators = []
        self.add_unit()
        self.type = 'Vehicle'

    def attack(self):
        attack_sum = [
            operator.attack()
            for operator in self.operators
            if operator.is_alive and operator.check_recharge
        ]
        if attack_sum:
            return 0.5 * (1 + self.health / 100) * count_gavg(attack_sum)
        else:
            return 0

    def add_unit(self):
        for item in range(self.operators_count):
            self.operators.append(
                Soldier(random.randint(50, 100), set_soldier_name))

    @property
    def is_alive(self):
        return self.health > 0 and self.count_operators_health > 0

    @property
    def count_operators_health(self):
        return sum([operator.health for operator in self.operators])/\
                     self.operators_count

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

    def count_health(self):
        if self.is_alive:
            return (self.count_operators_health + self.health)/2

    def damage(self):
        damage = 0.1 + sum([x.experience/100 for x in self.operators if x.check_recharge])
        return damage

    def damage_distribution(self):
        pass

    def recalculate_health(self):
        damage = self.damage()
        self.health = self.health - damage
