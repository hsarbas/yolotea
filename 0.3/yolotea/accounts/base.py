class AbstractAccount(object):

    def __init__(self, name, _id, _type):
        self.name = name
        self.id = _id
        self.type = _type

    def end_day(self):
        pass

    def take_order(self):
        pass
