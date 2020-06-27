class Card(object):

    def __init__(self, card):
        self._card = card

    @property
    def influence(self):
        return self._card.influence + \
               self._card.markers[InfluencePlusMarker] - \
               self._card.markers[InfluenceMinusMarker]


def get_outfits(group=None):
    """
    Returns a generator expression of all the Outfit cards in the group.
    :param group:
    :return: generator expression
    """
    return filter_cards(group, is_outfit)


def get_dudes(group=None):
    """
    Returns a generator expression of all the Dude cards in the group.
    :param group:
    :return: generator expression
    """
    return filter_cards(group, is_dude)


def filter_cards(group, filter_fn):
    if group is None:
        group = my_cards()
    return (card for card in group if filter_fn(card))


def is_outfit(card):
    """
    Returns True or False on whether card is an Outfit.
    :param card: A Card
    :return: bool
    """
    return card.type == 'Outfit'


def is_joker(card):
    """
    Returns True or False on whether card is a Joker.
    :param card: A Card
    :return: bool
    """
    return card.type == 'Joker'


def is_dude(card):
    """
    Returns True or False on whether card is a Dude.
    :param card: A Card
    :return: bool
    """
    return card.type == 'Dude'


def is_drifter(card):
    """
    Returns True or False on whether card is a Dude and is a Drifter
    :param card: A Card
    :return: bool
    """
    return is_dude(card) and card.outfit == 'Drifters'


def set_face_down(card):
    """
    Sets a card face down
    :param card:
    :return:
    """
    card.isFaceDown = True
    return card


def set_face_up(card):
    """
    Sets a card face up
    :param card:
    :return: card
    """
    card.isFaceDown = False
    return card

