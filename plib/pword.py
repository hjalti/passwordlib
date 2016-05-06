from string import printable as _printable
from random import choice

import os
import argparse

_symbol_index = _printable.index('~') + 1
_alnum_index = _printable.index('Z') + 1

_curr_dir = os.path.dirname(__file__)
with open(os.path.join(_curr_dir, 'words.txt')) as f:
    _words = list(filter(str.isalpha, f.read().splitlines()))


def pword(words=4, sep=' '):
    return sep.join( choice(_words) for _ in range(words) )

def rand_pass(length=8, use_symbols=True):
    index = [_alnum_index, _symbol_index][use_symbols]
    return ''.join( choice(_printable[:index]) for _ in range(length) )

def main():
    parser = argparse.ArgumentParser(description='Pass some words')
    parser.add_argument('--count', '-c', type=int, default=5)
    parser.add_argument('--words', '-w', type=int, default=pword.__defaults__[0])
    parser.add_argument('--seperator', '-s', default=pword.__defaults__[1])

    args = parser.parse_args()

    for _ in range(args.count):
        print(pword(args.words, args.seperator))

def rpass_main():
    parser = argparse.ArgumentParser(description='Pass some words')
    parser.add_argument('--count', '-c', type=int, default=5)
    parser.add_argument('--length', '-l', type=int, default=rand_pass.__defaults__[0])
    parser.add_argument('--only-alnum', '-o', action='store_false', default=rand_pass.__defaults__[1])

    args = parser.parse_args()

    for _ in range(args.count):
        print(rand_pass(args.length, args.only_alnum))

if __name__ == '__main__':
    main()
