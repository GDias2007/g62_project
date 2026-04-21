from classes.gclass import Gclass

class Transaction(Gclass):
    att = ['_transaction_id', '_transaction_date', '_amount', '_card_id']
    obj = dict()
    lst = list()
    pos = 0

    def __init__(self, transaction_id, transaction_date, amount, card_id):
        super().__init__()
        self._transaction_id = transaction_id
        self._transaction_date = transaction_date
        self._amount = amount
        self._card_id = card_id
        Transaction.obj[transaction_id] = self
        Transaction.lst.append(transaction_id)