import unittest

from phone_book.Class_work import methods


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_string = methods.Method("precious")
        my_string.get_string("precious")
        self.assertEqual("PRECIOUS", my_string.print_string())

    def test_something2(self):
        my_string = methods.Method("user_input   ")
        my_string.get_string("ayomide")
        self.assertEqual("AYOMIDE", my_string.print_string())


if __name__ == '__main__':
    unittest.main()
