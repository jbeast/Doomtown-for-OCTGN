import unittest
from mock import Mock, MagicMock

from deck import Deck
from deck_validator import DeckValidator


class TestDeckValidator(unittest.TestCase):
    def setUp(self):
        self.deck_validator = DeckValidator()
        self.empty_deck = Deck([])
        self.oversized_deck = Deck([Mock() for _ in range(60)])

        outfit = Mock()
        outfit.type = 'Outfit'
        self.multi_outfit_deck = [outfit, outfit]

        joker = Mock()
        joker.type = 'Joker'
        self.triple_joker_deck = [joker, joker, joker]

        nate_hunter = MagicMock()
        nate_hunter.type = 'Dude'
        nate_hunter.name = 'Nate Hunter'
        nate_hunter.__str__.return_value = nate_hunter.name
        self.over_four_copies_deck = [nate_hunter, nate_hunter, nate_hunter, nate_hunter, nate_hunter]

        self.really_erroneous_deck = self.multi_outfit_deck + self.triple_joker_deck + self.over_four_copies_deck

    def test_empty_deck(self):
        validation_result = self.deck_validator.validate(self.empty_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertIn('Deck has 0 cards! It should have 52 (plus Outfit and up to 2 Jokers).', validation_result.errors)

    def test_too_many_cards(self):
        validation_result = self.deck_validator.validate(self.oversized_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertIn('Deck has 60 cards! It should have 52 (plus Outfit and up to 2 Jokers).', validation_result.errors)

    def test_no_outfit(self):
        validation_result = self.deck_validator.validate(self.empty_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertIn('Deck has 0 Outfit cards. It should have 1!', validation_result.errors)

    def test_too_many_outfits(self):
        validation_result = self.deck_validator.validate(self.multi_outfit_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertIn('Deck has 2 Outfit cards. It should have 1!', validation_result.errors)

    def test_too_many_jokers(self):
        validation_result = self.deck_validator.validate(self.triple_joker_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertIn('Deck has 3 Jokers. It can only have up to 2!', validation_result.errors)

    def test_too_many_nate_hunters(self):
        validation_result = self.deck_validator.validate(self.over_four_copies_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertIn('Deck has 5 copies of "Nate Hunter". The maximum is 4!', validation_result.errors)

    def test_format(self):
        validation_result = self.deck_validator.validate(self.really_erroneous_deck)
        self.assertFalse(validation_result.is_valid)
        self.assertEqual('Deck has 5 cards! It should have 52 (plus Outfit and up to 2 Jokers).\n'
                         'Deck has 2 Outfit cards. It should have 1!\n'
                         'Deck has 3 Jokers. It can only have up to 2!\n'
                         'Deck has 5 copies of "Nate Hunter". The maximum is 4!',
                         validation_result.errors.format('\n'))


if __name__ == '__main__':
    unittest.main()
