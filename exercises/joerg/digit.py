import sys


translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

digit_str = sys.argv[1]

try:
    digit = int(digit_str)
    digit_translation = translation_table[digit]
except ValueError as e:
    print('this is not an integer:', digit_str)
    sys.exit(1)
except KeyError:
    print('this is not a digit:', digit)
    sys.exit(2)

print(digit_translation)
