def setup(group, x=0, y=0):
    """
    This function is usually the first one the player does. It will setup their home and cards on the left or right of the playfield
    It will also setup the starting Ghost Rock for the player according to the cards they bring in play, as well as their influence and CP.
    """
    mute()
    play_hand = my_play_hand()

    outfit = list(get_outfits(play_hand))

    if not len(outfit):
        whisper(":::ERROR::: You need to have an Outfit card in your hand before you try to setup the game. "
                "Please reset the board, load a valid deck and try again.")
        return

    starting_dudes = list(get_dudes(play_hand))
    if len(starting_dudes) > MAX_STARTING_DUDES:
        whisper(":::ERROR::: You can only start with a maximum of {} Dudes!".format(MAX_STARTING_DUDES))
        return

    for dude in starting_dudes:
        if dude.outfit != outfit[0].outfit and not is_drifter(dude):
            whisper(":::ERROR::: You can not start with a Dude that is not part of your Outfit or a Drifter!")
            return

    place_outfit(me, outfit[0])
    me.GhostRock = num(outfit[0].properties['Ghost Rock'])

    for dude in starting_dudes:
        place_dude(dude, face_down=True)
        pay(dude)

    hide(my_deck())
    shuffle(my_deck())

    notify("{} is playing {} and starting with {} dudes!".format(me, outfit[0], len(starting_dudes)))


def reveal_starting_dudes(group, x=0, y=0):
    mute()
    dudes = []

    for card in my_table_cards():
        set_face_up(card)
        dudes.append(card)

    notify("{} has revealed: {}".format(me, ",".join(dudes)))


def pay(card):
    mute()
    cost = num(card.cost)
    if cost == 0:
        return

    if me.GhostRock < cost:
        if not confirm("You do not seem to have enough Ghost Rock in your bank to play this card. "
                       "Are you sure you want to proceed? (If you do, your GR will become negative. "
                       "You will need to increase it manually as required.)"):
            notify("{} was supposed to pay {} Ghost Rock but only has {} in their bank.".format(me, cost, me.GhostRock))
            return

    me.GhostRock -= num(cost)
    notify("{} has paid {} Ghost Rock. {} is left in their bank".format(me, cost, me.GhostRock))