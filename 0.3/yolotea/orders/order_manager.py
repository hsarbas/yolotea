class OrderManager(object):

    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def delete_order(self, customer):
        pass

    def view_order(self, customer):
        ret = []
        for order in self.orders:
            if order.customer == customer:
                ret.append(order)
        return ret

    def view_all_orders(self):
        return self.orders
