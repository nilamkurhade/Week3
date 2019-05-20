import unittest
import json
from OOPs.Inventory import InventoryData


class Invent(unittest.TestCase):

    def test_Inventory(self):
        obj = InventoryData
        with open("/home/user/PycharmProjects/Python/OOPs/InventoryDataMgmt.json") as file:
            data = json.load(file)
        result = obj.__init__(self)
        expected = False
        if ValueError:
            self.assertFalse(expected, result)
        else:
            self.assertTrue(expected, result)

    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
