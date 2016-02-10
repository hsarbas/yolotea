import unittest
from yolotea.orders.concrete import *


class TestOrder(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_order_milktea(self):
        milktea = MilkTea('MilkTea', 'L', 100, 1, None, 'Harvs')
        self.assertEqual(milktea.flavor, 'MilkTea')
        self.assertEqual(milktea.size, 'L')
        self.assertEqual(milktea.sugar, 100)
        self.assertEqual(milktea.quantity, 1)
        self.assertEqual(milktea.sinkers, None)
        self.assertEqual(milktea.customer, 'Harvs')

    def test_order_fruittea(self):
        fruittea = FruitTea('Fruittea', 'L', 100, 1, None, 'Harvs')
        self.assertEqual(fruittea.flavor, 'Fruittea')
        self.assertEqual(fruittea.size, 'L')
        self.assertEqual(fruittea.sugar, 100)
        self.assertEqual(fruittea.quantity, 1)
        self.assertEqual(fruittea.sinkers, None)
        self.assertEqual(fruittea.customer, 'Harvs')

    def test_order_hottea(self):
        hottea = HotTea('Hottea', 'L', 1, 'Harvs')
        self.assertEqual(hottea.flavor, 'Hottea')
        self.assertEqual(hottea.size, 'L')
        self.assertEqual(hottea.sugar, None)
        self.assertEqual(hottea.quantity, 1)
        self.assertEqual(hottea.sinkers, None)
        self.assertEqual(hottea.customer, 'Harvs')

