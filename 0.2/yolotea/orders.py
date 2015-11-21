__author__ = 'Harvs'


class MilkTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.sugar = kwargs['sugar']
        self.quantity = kwargs['quantity']
        self.sinkers = kwargs['sinkers']
        self.customer = kwargs['customer']

    def serialize(self):
        return dict(flavor=self.flavor,
                    size=self.size,
                    sugar=self.sugar,
                    quantity=self.quantity,
                    sinkers=self.sinkers,
                    customer=self.customer)


class FruitTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.sugar = kwargs['sugar']
        self.quantity = kwargs['quantity']
        self.sinkers = kwargs['sinkers']
        self.customer = kwargs['customer']

    def serialize(self):
        return dict(flavor=self.flavor,
                    size=self.size,
                    sugar=self.sugar,
                    quantity=self.quantity,
                    sinkers=self.sinkers,
                    customer=self.customer)


class HotTea(object):

    def __init__(self, **kwargs):
        self.flavor = kwargs['flavor']
        self.size = kwargs['size']
        self.quantity = kwargs['quantity']
        self.customer = kwargs['customer']

    def serialize(self):
        return dict(flavor=self.flavor,
                    size=self.size,
                    quantity=self.quantity,
                    customer=self.customer)


class YoloSnack(object):

    def __init__(self, **kwargs):
        pass


class YoloCombo(object):

    def __init__(self, **kwargs):
        pass