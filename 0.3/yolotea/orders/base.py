class AbstractOrder(object):

    def __init__(self, flavor, size, sugar, quantity, sinkers, customer):
        self.flavor = flavor
        self.size = size
        self.sugar = sugar
        self.quantity = quantity
        self.sinkers = sinkers
        self.customer = customer
