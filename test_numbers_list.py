from unittest import TestCase
import numbers_list


class Test(TestCase):
    def test_sequential_list(self):
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        actual_output = numbers_list.sequential_list()
        self.assertEqual(expected_output, actual_output)

    def test_duplicate_sequential_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                           14, 15]
        actual_output = numbers_list.duplicate_sequential_list(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_eliminate_duplicate_values_in_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        actual_output = numbers_list.eliminate_duplicate_values_in_list(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_add_every_third_element_in_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_output = 45
        actual_output = numbers_list.add_every_third_element_in_list(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_add_first_middle_last_element_in_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_output = 24
        actual_output = numbers_list.add_first_middle_last_element_in_list(numbers)
        self.assertEqual(expected_output, actual_output)
