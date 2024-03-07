import unittest

import seven_segments
from seven_segments.seven_segment import SevenSegmentDisplay


class MyTestCase(unittest.TestCase):

    def test_display_horizontal(self):
        obj = SevenSegmentDisplay("111111011")
        self.assertRaises(RuntimeError, lambda: obj.put_in_a_list())

    def test_if_number_not_in_zero_and_one(self):
        obj = SevenSegmentDisplay("1112101")
        self.assertRaises(ValueError, lambda: obj.put_in_a_list())
