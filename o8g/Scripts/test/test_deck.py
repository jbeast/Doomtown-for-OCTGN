import unittest

from deck import Deck


class TestDeck(unittest.TestCase):
    def test_cards(self):
        cards = ['hi', 'there']
        deck = Deck(cards)
        self.assertEqual(deck.cards, cards)


if __name__ == '__main__':
    unittest.main()
