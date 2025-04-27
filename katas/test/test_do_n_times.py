import unittest
from unittest.mock import Mock
from katas.do_n_times import do_n_times

class TestDoNTimes(unittest.TestCase):
    def test_do_n_times_calls(self):
        mock_func = Mock()
        do_n_times(mock_func,5)
        self.assertEqual(mock_func.call_count,5)


    def test_do_n_times_zero_call(self):
        mock_func = Mock()
        do_n_times(mock_func,0)
        self.assertEqual(mock_func.call_count,0)


if __name__ == 'main':
    unittest.main()



