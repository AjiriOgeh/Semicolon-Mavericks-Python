from unittest import TestCase
import numbers_set


class Test(TestCase):
    def test_sum_collection(self):
        numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        expected_output = 55
        actual_output = numbers_set.sum_collection(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_remove_item(self):
        self.fail()

    def test_find_intersection(self):
        factors_of_twelve = {1, 2, 3, 4, 6, 12}
        factors_of_twenty = {1, 2, 4, 5, 10, 20}
        expected_output = {1, 2, 4}
        actual_output = numbers_set.find_intersection(factors_of_twelve, factors_of_twenty)
        self.assertEqual(expected_output, actual_output)
