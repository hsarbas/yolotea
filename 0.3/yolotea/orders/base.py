class AbstractOrder(object):

    def __init__(self, flavor, size, sugar, sinkers, customer):
        self.flavor = flavor
        self.size = size
        self.sugar = sugar
        self.sinkers = sinkers
        self.customer = customer
