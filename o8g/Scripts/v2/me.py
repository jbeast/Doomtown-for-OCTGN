from itertools import chain


def my_cards():
    chain(my_table_cards(), my_play_hand(), my_deck())


def my_table_cards():
    return (card for card in table_cards() if card.controller == me)


def my_deck():
    return me.Deck


def my_play_hand():
    return me.piles['Play Hand']