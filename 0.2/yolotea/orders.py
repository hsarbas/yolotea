__author__ = 'Windows User'


class MilkTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.sugar = kwargs['sugar']
        self.quantity = kwargs['quantity']
        self.sinkers = kwargs['sinkers']

    def serialize(self):
        return dict(flavor=self.flavor,
                    size=self.size,
                    sugar=self.sugar,
                    quantity=self.quantity,
                    sinkers=self.sinkers)


class FruitTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.sugar = kwargs['sugar']
        self.quantity = kwargs['quantity']
        self.sinkers = kwargs['sinkers']

    def serialize(self):
        return dict(flavor=self.flavor,
                    size=self.size,
                    sugar=self.sugar,
                    quantity=self.quantity,
                    sinkers=self.sinkers)


class HotTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.quantity = kwargs['quantity']

    def serialize(self):
        return dict(flavor=self.flavor,
                    size=self.size,
                    quantity=self.quantity)


class YoloSnack(object):

    def __init__(self, **kwargs):
        pass


class YoloCOmbo(object):

    def __init__(self, **kwargs):
        pass