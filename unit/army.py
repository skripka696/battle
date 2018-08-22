import datetime
import random
import time
from unit.squards import Squards
from unit.unit import SubUnit
from utils import set_squads_name

from battle.unit.solider import Soldier
from battle.unit.vehicle import Vehicle


class Army(SubUnit):
    """
    Army consists of squads
    """

    def __init__(self, name, strategy, squads, units):
        self.name = name
        self.strategy = strategy
        self.squads_count = squads
        self.squads = []
        self.add_unit(units)

    def add_unit(self, units):
        for item in range(self.squads_count):
            self.squads.append(
                Squards(set_squads_name(), self.strategy, units))

    def attack(self, opponent):
        time.sleep(1)
        print('********* ATTACK STARTED *********')
        attacking_squads = self.get_squad_by_strategy(self.strategy, self.squads)
        print('attacking squad - {}'.format(attacking_squads.name))
        opponent_squad = self.get_squad_by_strategy(self.strategy, opponent.squads)
        print('opponent squad - {}'.format(opponent_squad.name))

        attacking_squad = self.count_attacking_army(attacking_squads)
        opponent_damage = self.count_opponent_damage(opponent_squad)
        attacking_time = datetime.datetime.now()
        if attacking_squad and attacking_squad > opponent_damage:
            print('Opponent squad is died ')
            self.set_null_health(opponent_squad)
            self.increse_expirience(attacking_squads)
            self.set_recharge_time(attacking_squads, attacking_time)

        elif attacking_squad and attacking_squads < opponent_damage:
            damage_caused = attacking_squads - opponent_damage
            self.set_damage(damage_caused)
            self.set_recharge_time(attacking_squads, attacking_time)
            self.set_recharge_time(opponent_squad, attacking_time)

    def set_recharge_time(self, squad, attacking_time):
        for unit in squad.units:
            if unit.type == 'Soldier':
                unit.recharge = random.randint(100, 2000)
                unit.attack_time = attacking_time
            elif unit.type == 'Vehicle':
                unit.recharge = random.randint(1000, 2000)
                unit.attack_time = attacking_time
                for operator in unit.operators:
                    operator.recharge = random.randint(100, 2000)
                    operator.attack_time = attacking_time

    def set_damage(self, damage, squad):
        print('--------')

    def set_null_health(self, squad):
        for unit in squad.units:
            if unit.type == 'Soldier':
                unit.health = 0
            elif unit.type == 'Vehicle':
                unit.health = 0
                for operator in unit.operators:
                    operator.health = 0

    def increse_expirience(self, squad):
        for unit in squad.units:
            if unit.type == 'Soldier':
                unit.experience += 1
            elif unit.type == 'Vehicle':
                for operator in unit.operators:
                    operator.experience +=1

    def get_squad_by_strategy(self, strategy, squads):
        if strategy == 'strongest':
            max_health = max([x.health for x in squads])
            return [x for x in squads if x.health == max_health][0]
        elif strategy == 'weakest':
            min_health = max([x.health for x in squads])
            return [x for x in squads if x.health == min_health][0]
        else:
            return random.choice(squads)

    def count_opponent_damage(self, opponent):
        opponent_damage = opponent.damage()
        print('damage value - {}'.format(opponent_damage))
        return opponent_damage

    def count_attacking_army(self, attackin_squads):
        gavg_attack = attackin_squads.attack()
        print('attack value - {}'.format(gavg_attack))
        return gavg_attack

    @property
    def is_alive(self):
        return sum([squad.is_alive for squad in self.squads]) > 0

    @property
    def health(self):
        return sum([squad.health
                for squad in self.squads])