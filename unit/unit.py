from abc import abstractmethod


class Unit:
    """
    Each unit represents either a soldier or a vehicle maned
    """

    @abstractmethod
    def count_health(self):
        """
        Represents the health of the unit
        :return: range % [0-100]
        """
        pass

    @abstractmethod
    def check_recharge(self):
        """
        Represents the number of ms required to recharge the unit for an attack
        :return: range [100-2000]
        """
        pass


    @abstractmethod
    def attack(self):
        """
        Attack logic
        :return: attack_value
        """
        raise NotImplementedError('attack must be implemented in inherited class')

    @abstractmethod
    def damage(self):
        """
        Damage logic
        :return:  damage_value
        """
        raise NotImplementedError('damage must be implemented in inherited class')

    @abstractmethod
    def recalculate_health(self):
        pass

    def calculate_damage(self, damage, health):
        return self._percentage(damage, health)

    def _percentage(percent, whole):
        return int((percent * whole) / 100.0)


class SubUnit:
    @abstractmethod
    def generate_unit(self):
        """
        generation of nested units for different entities,
        such as Vehicle, Squads and Army
        :return:
        """
        raise NotImplementedError('generate_unit must be implemented in inherited class')