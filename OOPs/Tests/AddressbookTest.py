import unittest

from OOPs.AddressBook import AddressBook


class Invent(unittest.TestCase):

    def test_Inventory(self):
        obj = AddressBook()
        result = obj.address_book()
        expected = True
        if ValueError:
            self.assertFalse(expected, result)
        else:
            self.assertTrue(expected, result)

    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
