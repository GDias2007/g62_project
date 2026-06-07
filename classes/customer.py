from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_name', '_nif', '_email', '_bank_id']
    header = 'Customer'
    des = ['Id', 'Name', 'NIF', 'Email', 'Bank Id']

    def __init__(self, id, name, nif, email, bank_id):
        super().__init__()
        id = Customer.get_id(id)
        self._id = id
        self._name = name
        self._nif = int(nif)
        self._email = email
        self._bank_id = int(bank_id)
        Customer.obj[id] = self
        Customer.lst.append(id)

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
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, nif):
        self._nif = int(nif)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        self._bank_id = int(bank_id)
