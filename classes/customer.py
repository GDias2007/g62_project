from classes.gclass import Gclass

class Customer(Gclass):
    # Seguindo o novo diagrama: customer_id, name, nif, email e bank_id
    att = ['_customer_id', '_name', '_nif', '_email', '_bank_id']
    obj = dict()
    lst = list()
    pos = 0

    def __init__(self, customer_id, name, nif, email, bank_id):
        super().__init__()
        self._customer_id = customer_id
        self._name = name
        self._nif = nif
        self._email = email
        self._bank_id = bank_id # Ligação ao Banco segundo o novo diagrama
        
        Customer.obj[customer_id] = self
        Customer.lst.append(customer_id)