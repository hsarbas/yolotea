import os


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

    def create_file(self):
        path, dirs, files = os.walk("files/orders/").next()
        file_count = len(files)

        f = open('files/orders/' + str(file_count) + '.txt', 'w')

        for order in self.orders:
            f.write('Flavor: ' + order.flavor + '\n')
            f.write('Size: ' + order.size + '\n')
            f.write('Sugar Level: ' + order.sugar + '\n')
            f.write('Sinkers:' + '\n')
            for sinker in order.sinkers:
                f.write(sinker['name'] + ': ' + sinker['quantity'] + '\n')
            f.write('Customer: ' + order.customer + '\n' + '\n')

    def delete_all_files(self):
        pass
