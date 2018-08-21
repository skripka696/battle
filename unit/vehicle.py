from unit.unit import Unit


class Vehicle(Unit):
    """
    battle vehicle has these additional properties:

    Property  | Range | Description
    __________________________________________________________________________

    operators | [1-3] | The number of soldiers required to operate the vehicle
    """
    def __init__(self, health, recharge, operators):
        self.health = health
        self.recharge = recharge
        self.operators = operators

    def attack(self):
        return 0.5 * (1 + self.health / 100) * gavg(operator.attack_success)

    def damage(self):
        """Сумма ущерба, нанесенного солдату, рассчитывается следующим образом:"""
        damage = 0.05 + self.experience / 100
        return self.calculate_damage(damage, self.health)

    def recalculate_health(self):
        damage = self.damage()
        self.health = self.health - damage
