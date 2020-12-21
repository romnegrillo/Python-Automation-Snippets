import unittest
from check_valid_email import check_valid_email

class CheckValidEmailTest(unittest.TestCase):

    def test_basic(self):
        test_case = "romnegrillo@gmail.com"
        output = True

        self.assertEqual(check_valid_email(test_case), output)

    def test_incomplete(self):
        test_case = "romnegrillo@gmail"
        output = False

        self.assertEqual(check_valid_email(test_case), output)


unittest.main()
