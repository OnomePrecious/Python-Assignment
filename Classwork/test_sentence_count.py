import unittest

from Classwork import sentence_count


class MyTestCase(unittest.TestCase):
    def test_accept_sentence(self):
        sentence = "Hello world! 123"
        result = "LETTERS10, DIGITS3"
        self.assertEqual(sentence_count.accept_sentence(sentence), result)


if __name__ == '__main__':
    unittest.main()
