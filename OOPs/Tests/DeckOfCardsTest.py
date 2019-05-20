import unittest

from OOPs.DeckOfCards import DeckOfCard


class Invent(unittest.TestCase):

    def test_Inventory(self):
        obj = DeckOfCard()
        result = obj.dec_card()
        expected = False
        if ValueError:
            self.assertFalse(expected, result)
        else:
            self.assertTrue(expected, result)

    def test_deck_of_card_assign_to_players(self):
        obj = DeckOfCard()
        result = obj.dec_card()
        expected = False
        if ValueError:
            self.assertFalse(expected, result)
        else:
            self.assertTrue(expected, result)

    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
