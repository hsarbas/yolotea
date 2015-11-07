__author__ = 'Windows User'


class MilkTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.sugar = kwargs['sugar']
        self.quantity = kwargs['quantity']
        self.sinkers = kwargs['sinkers']


class FruitTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.sugar = kwargs['sugar']
        self.quantity = kwargs['quantity']
        self.sinkers = kwargs['sinkers']


class HotTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.quantity = kwargs['quantity']


class YoloSnack(object):

    def __init__(self, **kwargs):
        pass


class YoloCOmbo(object):

    def __init__(self, **kwargs):
        pass