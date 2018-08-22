import random

import time
from configs import set_game_config

from generate_data import army_generator
from unit.army import Army
from utils import set_army_name


class Game:

    def __init__(self, army_count, squads, strategy, units):
        self.army_count = army_count
        self.squads = squads
        self.strategy = strategy
        self.units = units
        self.round_count = 0
        self.game_finished = False
        self.armies = []

    def set_army_name(self):
        return 'Army_{}'.format(random.choice(army_generator))

    def generate_army(self):
        for army in range(self.army_count):
            self.armies.append(Army(
                set_army_name(),
                self.strategy,
                self.squads,
                self.units
            ))

    def choice_opponent(self, current_army):
        opponents = [army_opponent
                     for army_opponent in self.armies
                     if army_opponent is not
                     current_army and
                     army_opponent.is_alive
                     ]
        if opponents:
            return opponents

    def game_stop(self, army):
        for i in range(3):
            time.sleep(1)
            print('.')
        print('GAME_STOP. Win - {} army'.format(army.name))
        return

    def start_game(self):
        print('********* START GAME *********')
        self.generate_army()
        print('your game strategy is {}'.format(self.strategy))
        print('Generate {} armies'.format(len(self.armies)))
        while not self.game_finished:
            self.round_count += 1
            print('START ROUND {}'.format(self.round_count))
            for army in self.armies:
                opponents = self.choice_opponent(army)
                if not opponents:
                    self.game_finished = True
                    self.game_stop(army)
                    break
                else:
                    opponent = random.choice(self.choice_opponent(army))
                    army.attack(opponent)


def main():
    game_data = set_game_config()
    game = Game(army_count=game_data.get('army'),
                squads=game_data.get('squads'),
                strategy=game_data.get('strategy'),
                units=game_data.get('units'))
    game.start_game()


if __name__ == '__main__':
    main()

