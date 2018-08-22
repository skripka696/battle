import argparse
import random

strategy_data = {
        0: 'random',
        1: 'weakest',
        2: 'strongest'
    }


def set_army_count(army=None):
    if army and army >= 2:
        army_count = army
        print('**Army count set {}**'.format(army_count))
    else:
        army_count = random.randint(2, 10)
        print('**Army must be int and n>=2. Set {} number of army**'.format(army_count))
    return army_count


def set_strategy(strategy=None):
    if strategy and strategy >= 0 and strategy <=2:
        strategy_type = strategy_data.get(strategy)
        print('**Strategy set {}**'.format(strategy_type))
    else:
        strategy_type = strategy_data.get(random.randint(1, 3))
        print('**Strategy must be choice between 0-random, 1-weakest, 2-strongest.'
              ' Set {} strategy**'.format(strategy_type))
    return strategy_type


def set_squads_count(squads=None):
    if squads and squads >= 2:
        squads_count = squads
        print('**Squads count set {}**'.format(squads_count))
    else:
        army_count = random.randint(2, 10)
        print('**Squads must be int and n>=2. Set {} number of squads**'.format(army_count))
    return army_count


def set_unit_count_for_squads(units=None):
    if units and units >= 5 and units <= 10:
        units_count = units
        print('**Units count set {}**'.format(units_count))
    else:
        units_count = random.randint(5, 10)
        print('**Units must be 5 <= n <= 10. Set {} number of squads**'.format(units_count))
    return units_count


def set_game_config():
    parser = argparse.ArgumentParser(
        description='Set config for game',
    )

    parser.add_argument('-a', action='store', type=int, dest='army',
                        help='The number of armies: 2 <= n')

    parser.add_argument('-st', action='store', type=int, dest='strategy',
                        help='Choice of attack strategy: 0-random, 1-weakest, 2-strongest')
    parser.add_argument('-sq', action='store', type=int, dest='squads_count',
                        help='The number of squads per army: 2 <= n')
    parser.add_argument('-u', action='store', type=int, dest='units_count',
                        help='The number of units per squad: 5 <= n <= 10')

    args = parser.parse_args()
    game_data = dict(
        army=set_army_count(args.army),
        strategy=set_strategy(args.strategy),
        squads=set_squads_count(args.squads_count),
        units=set_unit_count_for_squads(args.units_count))

    return game_data