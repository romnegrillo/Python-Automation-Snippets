import unittest
import replace_domain

class IsEmalDomainExistsTest(unittest.TestCase):
    def test_simple(self):
        testcase = "romnegrillo@gmail.com"
        expected = True
        self.assertEqual(replace_domain.is_email_domain_exists(testcase, "gmail"), expected)

    def test_loop(self):
        test_dict = {
            "romnegrillo@gmail.com": True,
            "rom.negrillo@gmail.com": True,
            "rom-negrillo@gmail.com": True,
            "gmail.com@gmail.com": True,
        }

        for key, value in test_dict.items():
            testcase = key
            expected = value

            self.assertEqual(replace_domain.is_email_domain_exists(testcase, "gmail"), expected)

class ReplaceEmailDomainTest(unittest.TestCase):
    def test_loop(self):
        test_dict = {
            "romnegrillo@gmail.com": "romnegrillo@hunter.com",
            "rom.negrillo@gmail.com":    "rom.negrillo@hunter.com",
            "rom-negrillo@gmail.com":  "rom-negrillo@hunter.com",
            "gmail.com@gmail.com": "gmail.com@hunter.com"
        }

        for key, value in test_dict.items():
            testcase = key
            expected = value

            self.assertEqual(replace_domain.replace_email_domain(testcase, "hunter"), expected)


unittest.main()