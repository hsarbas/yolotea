from base import AbstractAccount


class Admin(AbstractAccount):

    def __init__(self, name, _id):
        super(Admin, self).__init__(name, _id, 'admin')

    def view_accounts(self):
        pass

    def view_sales(self):
        pass

    def view_inventory(self):
        pass


class Cashier(AbstractAccount):

    def __init__(self, name, _id):
        super(Cashier, self).__init__(name, _id, 'cashier')
