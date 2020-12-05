import unittest

from advent.day2 import sled_rental_password_validity, toboggan_password_validity


class TestDay2Solution(unittest.TestCase):
    def setUp(self):
        self.sled_policy_data = {
            "1-3 a: abcde": 1,
            "1-3 b: cdefg": 0,
            "2-9 c: ccccccccc": 1,
        }
        self.toboggan_policy_data = {
            "1-3 a: abcde": 1,
            "1-3 b: cdefg": 0,
            "2-9 c: ccccccccc": 0,
        }
        self.part_one_answer = 2

    def test_day_02_part_one(self):
        for password_policy, validity in self.sled_policy_data.items():
            self.assertEqual(sled_rental_password_validity(password_policy), validity)

    def test_day_02_part_two(self):
        for password_policy, validity in self.toboggan_policy_data.items():
            self.assertEqual(toboggan_password_validity(password_policy), validity)


if __name__ == "__main__":
    unittest.main(verbosity=2)