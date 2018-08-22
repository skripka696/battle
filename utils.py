import random
import numpy

from generate_data import name_generator, squads_generator,\
    army_generator


def count_gavg(data):
    """
    calculate geometric avarage from list
    :param data:
    :return:
    """
    data_count = len(data)
    data_composition = numpy.prod(numpy.array(data))

    gavg = data_composition ** (1/data_count)

    return gavg


def set_soldier_name():
    return 'Solider_{}_{}'.format(
        random.choice(name_generator),
        random.randint(1, 1000)
    )


def set_vehicle_name():
    return 'Vehicle_{}_{}'.format(
        random.choice(name_generator),
        random.randint(1, 1000)
    )


def set_squads_name():
    return 'Squads_{}_{}'.format(
        random.choice(squads_generator),
        random.randint(1, 1000)
    )


def set_army_name():
    return 'Army_{}_{}'.format(
        random.choice(army_generator),
        random.randint(1, 1000)
    )