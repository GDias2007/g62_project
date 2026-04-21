from classes.gclass import Gclass

class Card(Gclass):
    att = ['_card_id', '_name', '_card_type']
    obj = dict()
    lst = list()
    pos = 0

    def __init__(self, card_id, name, card_type):
        super().__init__()
        self._card_id = card_id
        self._name = name
        self._card_type = card_type
        Card.obj[card_id] = self
        Card.lst.append(card_id)