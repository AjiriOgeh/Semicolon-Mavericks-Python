from unittest import TestCase
import seven_segments_display


class Test(TestCase):

    def test_display_character_with_seven_digits(self):
        with self.assertRaises(ValueError):
            seven_segments_display.display_seven_segment("1010110")

    def test_display_character_with_non_binary_digits(self):
        with self.assertRaises(ValueError):
            seven_segments_display.display_seven_segment("12002201")

    def test_display_character_with_non_numeric_digits(self):
        with self.assertRaises(ValueError):
            seven_segments_display.display_seven_segment("100ABC01")

    def test_display_character_8(self):
        self.assertEqual("n", seven_segments_display.display_seven_segment("11111111"))





