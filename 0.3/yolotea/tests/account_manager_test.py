import unittest
from yolotea.accounts.account_manager import AccountManager


class AccountManagerTest(unittest.TestCase):

    def setUp(self):
        self.manager = AccountManager()

    def tearDown(self):
        del self.manager

    def test_add_account(self):

        self.manager.add_account('account1', '1', '123', 'admin')
        self.manager.add_account('account2', '2', '123', 'cashier')
        self.manager.add_account('account3', '3', '123', 'cashier')

    # def test_delete_account(self):
    #     self.manager.delete_account(2)
    #     self.manager.delete_account(1)
    #     self.manager.delete_account(3)
