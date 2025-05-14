import unittest
import time
from katas.time_me import measure_execution_time  # Replace with your actual module name

class TestMeasureExecutionTime(unittest.TestCase):

    def test_sample_function_time(self):
        def sample_function():
            time.sleep(0.5)

        elapsed = measure_execution_time(sample_function)
        self.assertGreaterEqual(elapsed, 480)
        self.assertLess(elapsed, 520)

    def test_quick_function_time(self):
        def quick_function():
            pass

        elapsed = measure_execution_time(quick_function)
        self.assertIsInstance(elapsed, float)
        self.assertGreaterEqual(elapsed, 0)

    def test_short_sleep(self):
        def short_sleep():
            time.sleep(0.1)

        elapsed = measure_execution_time(short_sleep)
        self.assertGreaterEqual(elapsed, 90)
        self.assertLess(elapsed, 110)

    def test_function_raises_exception(self):
        def faulty_function():
            raise ValueError("This is a test error")

        with self.assertRaises(ValueError):
            measure_execution_time(faulty_function)

    def test_return_type(self):
        elapsed = measure_execution_time(lambda: None)
        self.assertIsInstance(elapsed, float)

    def test_time_is_non_negative(self):
        elapsed = measure_execution_time(lambda: None)
        self.assertGreaterEqual(elapsed, 0)


if __name__ == '__main__':
    unittest.main()
