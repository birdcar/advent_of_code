import unittest

from advent.day1 import find_complement_values


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

        self.test_answer = 514579

    def test_find_complement_values(self):
        x, y = find_complement_values(self.test_input, 2020)
        self.assertEqual(x * y, self.test_answer)


if __name__ == "__main__":
    unittest.main()