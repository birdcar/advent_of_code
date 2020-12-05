import unittest

from advent.day1 import find_n_complement_values


class TestDay1Solution(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]
        self.test_answer_part_one = 514579
        self.test_answer_part_two = 241861950

    def test_day_01_part_one(self):
        x, y = find_n_complement_values(self.test_input, 2020, 2)
        self.assertEqual(x * y, self.test_answer_part_one)

    def test_day_01_part_two(self):
        x, y, z = find_n_complement_values(self.test_input, 2020, 3)
        self.assertEqual(x * y * z, self.test_answer_part_two)


if __name__ == "__main__":
    unittest.main(verbosity=2)