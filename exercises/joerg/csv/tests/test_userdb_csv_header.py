import userdb_csv
import sys


def test_user_attribute(tmpdir):
    filename = tmpdir / 'test.csv'

    # fixture >>>
    f = open(filename, 'w', encoding='cp1252')
    f.write('\n'.join([
        'ID;First name;Last name;Date of Birth',
        '1;"Jörg;DI";Faschingbauer;19.6.1966',
        '2;Caro;Faschingbauer;25.4.1997',
        '3;Johanna;Faschingbauer;11.6.1995',
        '4;Philipp;Lichtenberger;6.4.1986',
        '5;Elizabeth II;Queen;1.1.1900',
    ]))
    f.close()
    # <<< fixture


    users = userdb_csv.read_csv_header(filename)
    assert type(users) is list, users
    assert len(users) == 5, len(users)
    
    assert users[0].id == 1
    assert users[0].firstname == 'Jörg;DI'
    assert users[0].lastname == 'Faschingbauer'
    assert users[0].birth == '19.6.1966'
    
    assert users[1].id == 2
    assert users[1].firstname == 'Caro'
    assert users[1].lastname == 'Faschingbauer'
    assert users[1].birth == '25.4.1997'
    
    assert users[2].id == 3
    assert users[2].firstname == 'Johanna'
    assert users[2].lastname == 'Faschingbauer'
    assert users[2].birth == '11.6.1995'
    
    assert users[3].id == 4
    assert users[3].firstname == 'Philipp'
    assert users[3].lastname == 'Lichtenberger'
    assert users[3].birth == '6.4.1986'
    
    assert users[4].id == 5
    assert users[4].firstname == 'Elizabeth II'
    assert users[4].lastname == 'Queen'
    assert users[4].birth == '1.1.1900'

def test_fullname(tmpdir):
    filename = tmpdir / 'test.csv'

    # fixture >>>
    f = open(filename, 'w', encoding='cp1252')
    f.write('\n'.join([
        'ID;First name;Last name;Date of Birth',
        '2;Caro;Faschingbauer;25.4.1997',
    ]))
    f.close()
    # <<< fixture

    users = userdb_csv.read_csv_header(filename)
    assert users[0].fullname == 'Caro Faschingbauer'

