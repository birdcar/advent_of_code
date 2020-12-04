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

    def test_find_2_complement_values(self):
        """
        Correctly find the two entries that sum to 2020 in the test data
        """
        x, y = find_n_complement_values(self.test_input, 2020, 2)
        self.assertEqual(x * y, self.test_answer_part_one)

    def test_find_3_complement_values(self):
        """
        Correctly find the three entries that sum to 2020 in the test data
        """
        x, y, z = find_n_complement_values(self.test_input, 2020, 3)
        self.assertEqual(x * y * z, self.test_answer_part_two)

    def test_no_target_found_zero(self):
        """
        If the target value cannot be found in the input list, then
        find_n_complement_values should return a tuple of zeroes equal to the
        argument passed to n_terms
        """
        self.assertEqual(find_n_complement_values(self.test_input, 0, 2), (0, 0))
        self.assertEqual(find_n_complement_values(self.test_input, 0, 3), (0, 0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)