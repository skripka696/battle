from abc import ABC, abstractmethod

class Unit:
    """
    Each unit represents either a soldier or a vehicle maned
    """

    @abstractmethod
    def set_health(self):
        """
        Represents the health of the unit
        :return: range % [0-100]
        """
        pass

    @abstractmethod
    def set_recharge(self):
        """
        Represents the number of ms required to recharge the unit for an attack
        :return: range [100-2000]
        """
        pass

    @abstractmethod
    def set_name(self):
        """
        Unit name
        :return: unit_name
        """
        raise NotImplementedError('set_name must be implemented in inherited class')


    @abstractmethod
    def attack(self):
        """
        Attack logic
        :return: attack_value
        """
        pass

    @abstractmethod
    def damage(self):
        """
        Damage logic
        :return:  damage_value
        """
        pass

    @abstractmethod
    def infliction_attack(self):
        """
        Inflicted attack
        :return: percent attack_value
        """
        pass

    @abstractmethod
    def infliction_damage(self):
        """
        Inflicted damage
        :return: percent damage_value
        """
        pass

    @abstractmethod
    def recalculate_health(self):
        pass

    def calculate_damage(self, damage, health):
        return self._percentage(damage, health)

    def _percentage(percent, whole):
        return int((percent * whole) / 100.0)