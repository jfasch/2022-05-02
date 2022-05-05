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

rdr = csv.reader(f, delimiter=':')

for username, password, uid, gid, description, home, shell in rdr:
    userdatabase[username] = {
        'uid': uid,
        'gid': gid,
        'home': home,
        'shell': shell,
    }

# pprint.pprint(userdatabase)

for user in usernames:
    pprint.pprint(userdatabase[user])
