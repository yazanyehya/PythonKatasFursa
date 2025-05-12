import unittest
from katas.stock_trader import max_profit

class TestStockTrader(unittest.TestCase):
    def test_normal_case(self):
        stock_prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(stock_prices),5)

    def test_sorted_array(self):
        stock_prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(stock_prices),4)

    def test_reverse_sorted_array(self):
        stock_prices = [5,4,3,2,1]
        self.assertEqual(max_profit(stock_prices), 0)

    def test_one_element(self):
        stock_prices = [1]
        self.assertEqual(max_profit(stock_prices), 0)

    def test_two_element(self):
        stock_prices = [1,10]
        self.assertEqual(max_profit(stock_prices), 9)

    def test_two_element1(self):
        stock_prices = [10,1]
        self.assertEqual(max_profit(stock_prices), 0)


if __name__ == '__main__':
    unittest.main()

