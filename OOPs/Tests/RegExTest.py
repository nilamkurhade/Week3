import unittest
from OOPs.RegEx import RegularExpression


class RegExp(unittest.TestCase):

    def test_RegEx(self):

        obj = RegularExpression
        # Returns True or False.

        result = obj.regular_expression(obj.self)
        expected = True
        if ValueError:
            self.assertFalse(expected, result)
        else:
            self.assertTrue(expected, result)

    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()



