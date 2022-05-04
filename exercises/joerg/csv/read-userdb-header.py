import csv
import sys

filename = sys.argv[1]

f = open(filename, encoding='cp1252')
rdr = csv.DictReader(f, delimiter=';', quotechar='"')
for record in rdr:
    id, firstname, lastname, birth = record.values()
    print(f"ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth:{birth}")
