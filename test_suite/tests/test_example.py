# This is a quick example test file to show how tests can be set up.

import unittest


class TestExample(unittest.TestCase):  # Your test class is a subclass of unittest.Testcase, this is important
    """
    `Test Example Notes:`

        This is a mock test class to model tests after.
        The setUp method MUST be in camel-case for every test file. Everything else can be in snake_case as normal.

        The command to run tests is:
            ``python -m test_suite.runner``
    """

    def setUp(self):
        """
        This method is used to set up anything you wish to test prior to every test method below.
        :return:
        """
        # Setting up a quick dictionary, for example
        # Any changes made to anything built in setUp DO NOT carry over to later test methods

        self.d = {
            "string": "Hello World!",
            "array": [1, 2, 3, 4, 5],
            "integer": 42,
            "bool": False
        }

    # Test methods should always start with the word 'test'
    def test_dict_array(self):
        a = self.d["array"]

        self.assertEqual(a, [1, 2, 3, 4, 5])
        self.assertEqual(a[2], 3)
        self.assertIn(5, a)

    def test_dict_string(self):
        s = self.d["string"]
        self.assertIn("Hello", s)
        self.assertNotEqual("Walkin' on the Sun", s)

    def test_dict_integer(self):
        i = self.d["integer"]
        self.assertGreater(50, i)

        # Checks within 7 decimal points
        self.assertAlmostEqual(i, 42.00000001)

    def test_dict_bool(self):
        b = self.d["bool"]
        self.assertFalse(b)
        self.assertEqual(b, False)

    # This is just the very basics of how to set up a test file
    # For more info: https://docs.python.org/3/library/unittest.html


if __name__ == '__main__':
    unittest.main
