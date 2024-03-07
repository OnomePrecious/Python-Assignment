import unittest

from phone_book.Class_work import sequential_list


class MyTestCase(unittest.TestCase):
    def test_elements_is_added_at_third_position(self):
        sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sample_out = 18
        self.assertEqual(sequential_list.add_third_elements(sample_list), sample_out)

    def test_that_sum_of_elements_is_returned(self):
        sample_set =( 1, 2, 3, 4, 5, 6,)
        sample_out = 21
        self.assertEqual(sequential_list.sum_collection(sample_set), sample_out)


