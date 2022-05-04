import csv

class User:
    def __init__(self, id, firstname, lastname, birth):
        assert type(id) is int
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

    @property
    def fullname(self):
        if not hasattr(self, '_fullname'):
            self._fullname = self.firstname + ' ' + self.lastname
        return self._fullname

def read_csv_header(filename):
    users = []

    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')
    for record in rdr:
        u = User(id=int(record['ID']),
                 firstname=record['First name'],
                 lastname=record['Last name'],
                 birth=record['Date of Birth'])
        users.append(u)

    return users
