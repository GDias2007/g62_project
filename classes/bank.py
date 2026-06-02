"""
@author: Grupo 62 (2025)
#objective: class Bank
"""
from classes.gclass import Gclass

class Bank(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_designation', '_founding_date']
    header = 'Bank'
    des = ['Id', 'Designation', 'Founding Date']

    def __init__(self, id, designation, founding_date):
        super().__init__()
        id = Bank.get_id(id)
        self._id = id
        self._designation = designation
        self._founding_date = founding_date
        Bank.obj[id] = self
        Bank.lst.append(id)

    @property
    def id(self):
        return self._id

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, designation):
        self._designation = designation

    @property
    def founding_date(self):
        return self._founding_date

    @founding_date.setter
    def founding_date(self, founding_date):
        self._founding_date = founding_date
