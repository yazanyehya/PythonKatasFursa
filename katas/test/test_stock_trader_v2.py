import unittest
from katas.stock_trader_v2 import max_profit  # Adjust path to your file

class TestMaxProfitMultipleTransactions(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 7)  # Correct total: 4 (1→5) + 3 (3→6)

    def test_ascending_prices(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)  # 1→2→3→4→5

    def test_descending_prices(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)  # No gain

    def test_fluctuating_prices(self):
        self.assertEqual(max_profit([3, 2, 6, 5, 0, 3]), 7)  # 2→6 (4), 0→3 (3)

    def test_single_day(self):
        self.assertEqual(max_profit([5]), 0)  # Not enough days to make profit

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)  # No data, no profit

if __name__ == '__main__':
    unittest.main()
