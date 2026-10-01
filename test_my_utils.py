import unittest
import my_utils
import random
import statistics
from math import sqrt


class TestCalc(unittest.TestCase):
    def test_mean_basic(self):
        # It is acceptable for this to output either a float or int
        self.assertAlmostEqual(my_utils.mean([4, 5.0, 2, 1, 3]), 3, places=5)

    def test_mean_empty(self):
        self.assertRaises(SystemExit, my_utils.mean, [])

    def test_mean_nonnumeric(self):
        self.assertRaises(SystemExit, my_utils.mean, [4, 5.0, 2, 1, "3"])

    def test_mean_single(self):
        # It is acceptable for this to output either a float or int
        self.assertAlmostEqual(my_utils.mean([1.0]), 1)

    def test_mean_random(self):
        # As processing is likely slightly different, almost equal will suffice
        length = random.randint(1, 100)
        array = [random.randint(1, 100) for _ in range(length)]
        self.assertAlmostEqual(my_utils.mean(array), statistics.mean(array))

    def test_median_basic(self):
        # It is acceptable for this to output either a float or int
        self.assertAlmostEqual(my_utils.mean([4, 5.0, 2, 1, 3]), 3, places=5)

    def test_median_empty(self):
        self.assertRaises(SystemExit, my_utils.median, [])

    def test_median_nonnumeric(self):
        self.assertRaises(SystemExit, my_utils.median, [4, 5.0, 2, 1, "3"])

    def test_median_single(self):
        # It is acceptable for this to output either a float or int
        self.assertAlmostEqual(my_utils.mean([1.0]), 1)

    def test_median_random(self):
        # As processing is likely slightly different, almost equal will suffice
        length = random.randint(1, 100)
        array = [random.randint(1, 100) for _ in range(length)]
        self.assertAlmostEqual(my_utils.median(array),
                               statistics.median(array))

    def test_std_basic(self):
        # It is acceptable for this to output either a float or int
        self.assertAlmostEqual(my_utils.std([4, 5.0, 2, 1, 3]),
                               sqrt(2), places=5)

    def test_std_empty(self):
        self.assertRaises(SystemExit, my_utils.std, [])

    def test_std_nonnumeric(self):
        self.assertRaises(SystemExit, my_utils.std, [4, 5.0, 2, 1, "3"])

    def test_std_single(self):
        # It is acceptable for this to output either a float or int
        self.assertAlmostEqual(my_utils.mean([1.0]), 1)

    def test_std_random(self):
        # As processing is likely slightly different, almost equal will suffice
        length = random.randint(1, 100)
        array = [random.randint(1, 100) for _ in range(length)]
        self.assertAlmostEqual(my_utils.std(array), statistics.pstdev(array))


if __name__ == '__main__':
    unittest.main()
