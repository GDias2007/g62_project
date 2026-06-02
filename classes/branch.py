"""
@author: Grupo 62 (2025)
#objective: class Branch
"""
from classes.gclass import Gclass

class Branch(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_address', '_bank_id']
    header = 'Branch'
    des = ['Id', 'Address', 'Bank Id']

    def __init__(self, id, address, bank_id):
        super().__init__()
        id = Branch.get_id(id)
        self._id = id
        self._address = address
        self._bank_id = int(bank_id)
        Branch.obj[id] = self
        Branch.lst.append(id)

    @property
    def id(self):
        return self._id

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        self._bank_id = int(bank_id)
