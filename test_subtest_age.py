import unittest
from age import categorize_by_age


class TestChildAge(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 10):  # 0–9
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a child.")
                self.assertEqual(result, "Child")


class TestAdultAge(unittest.TestCase):
    def test_adult_age(self):
        for age in range(19, 66):  # 19–65
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as an adult.")
                self.assertEqual(result, "Adult")


class TestGoldenAge(unittest.TestCase):
    def test_golden_age(self):
        for age in range(66, 151):  # 66–150
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"{age} is considered as a golden age.")
                self.assertEqual(result, "Golden age")


if name == "main":
    unittest.main(verbosity=2)