from classes.gclass import Gclass

class Bank(Gclass):
    att = ['_bank_id', '_designation', '_founding_date']
    obj = dict()
    lst = list()
    pos = 0

    def __init__(self, bank_id, designation, founding_date):
        super().__init__()
        self._bank_id = bank_id
        self._designation = designation
        self._founding_date = founding_date
        Bank.obj[bank_id] = self
        Bank.lst.append(bank_id)
