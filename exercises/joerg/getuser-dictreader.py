import argparse
import pprint
import sys
import csv


# argument parsing section >>>
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='path to password file')
parser.add_argument('username', nargs='+', help='list of users to search for')

args = parser.parse_args()

filename = args.filename
usernames = args.username
# <<<

f = open(filename)

userdatabase = {}

rdr = csv.DictReader(f, fieldnames=['username', 'password', 'uid', 'gid', 'description', 'home', 'shell'], delimiter=':')

for userrecord in rdr:
    username = userrecord['username']
    del userrecord['description']
    del userrecord['password']
    del userrecord['username']
    userdatabase[username] = userrecord

pprint.pprint(userdatabase)

for user in usernames:
    pprint.pprint(userdatabase[user])
