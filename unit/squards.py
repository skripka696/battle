import random

from unit.solider import Soldier
from unit.unit import SubUnit
from unit.vehicle import Vehicle
from utils import set_soldier_name, set_vehicle_name, count_gavg


class Squards(SubUnit):

    """
    Squads are consisted out of a number of units (soldiers or vehicles),
    that behave as a coherent group.
    A squad is active as long as is contains an active unit.
    """

    def __init__(self, name, strategy, units):
        self.name = name
        self.strategy = strategy
        self.units_count = units
        self.units = []
        self.add_unit()

    def add_unit(self):
        solder_count = random.randint(1, self.units_count)
        vehicle_count = self.units_count - solder_count
        for item in range(solder_count):
            self.units.append(
                Soldier(random.randint(50, 100), set_soldier_name()))
        for item in range(vehicle_count):
            self.units.append(
                Vehicle(random.randint(50, 100), set_vehicle_name(),  random.randint(1, 3)))

    def attack(self):
        return count_gavg(
            [unit.attack()
             for unit in self.units
             if unit.is_alive and unit.check_recharge]
        )

    def damage(self):
        return count_gavg(
            [unit.damage()
             for unit in self.units
             if unit.is_alive and unit.check_recharge]
        )

    @property
    def health(self):
        return sum([unit.health
                    for unit in self.units])

    @property
    def is_alive(self):
        return sum([unit.is_alive for unit in self.units]) > 0

    def damage_distribution(self):
        pass