from collections import namedtuple


class DeckValidator(object):

    DECK_SIZE = 52

    def validate(self, deck):
        validation_errors = self.ValidationErrors()
        card_count = 0
        outfit_count = 0
        joker_count = 0
        card_counter = {}

        for card in deck:
            if is_outfit(card):
                outfit_count += 1
            elif is_joker(card):
                joker_count += 1
            else:
                card_count += 1

            if card not in card_counter:
                card_counter[card] = 1
            else:
                card_counter[card] += 1

        if card_count != self.DECK_SIZE:
            validation_errors.add(
                'Deck has {} cards! It should have 52 (plus Outfit and up to 2 Jokers).'.format(card_count)
            )

        if outfit_count != 1:
            validation_errors.add('Deck has {} Outfit cards. It should have 1!'.format(outfit_count))

        if joker_count > 2:
            validation_errors.add('Deck has {} Jokers. It can only have up to 2!'.format(joker_count))

        for card, count in card_counter.iteritems():
            if count > 4:
                validation_errors.add('Deck has {} copies of "{}". The maximum is 4!'.format(count, card))

        return self.ValidationResult(is_valid=validation_errors.is_empty(), errors=validation_errors)

    ValidationResult = namedtuple('ValidationResult', 'is_valid errors')

    class ValidationErrors:
        def __init__(self):
            self._errors = []

        def __len__(self):
            return len(self._errors)

        def __iter__(self):
            return iter(self._errors)

        def add(self, error):
            if error not in self._errors:
                self._errors.append(error)

        def is_empty(self):
            return len(self) == 0

        def format(self, separator):
            return separator.join(self._errors)
