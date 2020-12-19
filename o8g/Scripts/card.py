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