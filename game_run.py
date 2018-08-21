import argparse
import random

from configs import set_game_config


class Game:

    def __init__(self, army, squads, strategy, units):
        self.army_count = army
        self.squads = squads
        self.strategy = strategy
        self.units = units

    def generate_army(self):
        pass

    def generate_squads(self):
        pass

    def generate_vehicles(self):
        pass

    def generate_soldiers(self):
        pass

def main():
    game_data = set_game_config()
    game = Game(army=game_data.get('army'),
                squads=game_data.get('squads'),
                strategy=game_data.get('strategy'),
                units=game_data.get('units'))

    print(game_data)
main()

