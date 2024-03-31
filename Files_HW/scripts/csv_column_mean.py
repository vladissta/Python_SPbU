#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csvfile', type=argparse.FileType('r'))
parser.add_argument('column', type=int)
parser.add_argument('isheader', type=bool)

args = parser.parse_args()

s = 0
n = 0

column_number = int(args.column)

if args.isheader:
    colname = args.csvfile.readline().split(',')[column_number - 1]

try:
    for row in args.csvfile:
        s += int(row.split(',')[column_number - 1])
        n += 1
except ValueError:
    print('Column contains non-nummeric data')
else:
    print(f'Mean of {colname} = {s / n}')
