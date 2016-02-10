import unittest
from yolotea.accounts.concrete import Admin, Cashier


class TestAccount(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_admin(self):
        admin = Admin('admin_name', 1)
        self.assertEqual(admin.name, 'admin_name', 'Incorrect account name')
        self.assertEqual(admin.id, 1, 'Incorrect account id')
        self.assertEqual(admin.type, 'admin', 'Incorrect account type')

    def test_create_cashier(self):
        cashier = Cashier('cashier_name', 2)
        self.assertEqual(cashier.name, 'cashier_name', 'Incorrect account name')
        self.assertEqual(cashier.id, 2, 'Incorrect account id')
        self.assertEqual(cashier.type, 'cashier', 'Incorrect account type')
