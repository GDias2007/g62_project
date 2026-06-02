"""
@author: Grupo 62 (2025)
#objective: class Transaction
"""
from classes.gclass import Gclass

class Transaction(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_transaction_date', '_amount', '_card_id']
    header = 'Transaction'
    des = ['Id', 'Date', 'Amount', 'Card Id']

    def __init__(self, id, transaction_date, amount, card_id):
        super().__init__()
        id = Transaction.get_id(id)
        self._id = id
        self._transaction_date = transaction_date
        self._amount = float(amount)
        self._card_id = int(card_id)
        Transaction.obj[id] = self
        Transaction.lst.append(id)

    @property
    def id(self):
        return self._id

    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        self._transaction_date = transaction_date

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = float(amount)

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        self._card_id = int(card_id)
