from base import AbstractOrder


class MilkTea(AbstractOrder):

    def __init__(self, flavor, size, sugar, sinkers, customer):
        super(MilkTea, self).__init__(flavor, size, sugar, sinkers, customer)


class FruitTea(AbstractOrder):

    def __init__(self, flavor, size, sugar, sinkers, customer):
        super(FruitTea, self).__init__(flavor, size, sugar, sinkers, customer)


class HotTea(AbstractOrder):

    def __init__(self, flavor, size, customer):
        super(HotTea, self).__init__(flavor, size, None, None, customer)
