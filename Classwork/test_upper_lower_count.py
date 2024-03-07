import unittest

from Classwork import upper_lower_count


class MyTestCase(unittest.TestCase):
    def test_upper_lower_count(self):
        sentence = "Hello world!"
        result = "UPPERCASE1, LOWERCASE9"
        self.assertEqual(upper_lower_count.accept_sentence(sentence), result)
