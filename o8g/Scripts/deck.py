class Deck(object):

    def __init__(self, cards):
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __iter__(self):
        return iter(self._cards)
