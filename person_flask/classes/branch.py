from classes.gclass import Gclass

class Branch(Gclass):
    att = ['_branch_id', '_branch_location', '_bank_id']
    obj = dict()
    lst = list()
    pos = 0

    def __init__(self, branch_id, branch_location, bank_id):
        super().__init__()
        self._branch_id = branch_id
        self._branch_location = branch_location
        self._bank_id = bank_id
        Branch.obj[branch_id] = self
        Branch.lst.append(branch_id)