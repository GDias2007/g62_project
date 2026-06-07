from classes.gclass import Gclass

class Card(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_name', '_type', '_bank_id']
    header = 'Card'
    des = ['Id', 'Name', 'Type', 'Bank Id']

    def __init__(self, id, name, card_type, bank_id):
        super().__init__()
        id = Card.get_id(id)
        self._id = id
        self._name = name
        self._type = card_type
        self._bank_id = int(bank_id)
        Card.obj[id] = self
        Card.lst.append(id)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, card_type):
        self._type = card_type

    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        self._bank_id = int(bank_id)
