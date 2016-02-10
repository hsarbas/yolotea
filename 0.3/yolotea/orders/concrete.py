from base import AbstractOrder


class MilkTea(AbstractOrder):

    def __init__(self, flavor, size, sugar, quantity, sinkers, customer):
        super(MilkTea, self).__init__(flavor, size, sugar, quantity, sinkers, customer)


class FruitTea(AbstractOrder):

    def __init__(self, flavor, size, sugar, quantity, sinkers, customer):
        super(FruitTea, self).__init__(flavor, size, sugar, quantity, sinkers, customer)


class HotTea(AbstractOrder):

    def __init__(self, flavor, size, quantity, customer):
        super(HotTea, self).__init__(flavor, size, None, quantity, None, customer)
