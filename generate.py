#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import random
import string


def generate(max_count, max_length, const_count, const_length):
    if const_count:
        count = max_count
    else:
        count = random.randint(0, max_count)
    for _ in range(count):
        if const_length:
            length = max_length
        else:
            length = random.randint(0, max_length)
        yield "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
        )


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--max-count", type=int, required=True)
parser.add_argument("-l", "--max-length", type=int, required=True)
parser.add_argument("-C", "--const-count", help="Do not randomize lines count", action="store_true")
parser.add_argument("-L", "--const-length", help="Do not randomize line length", action="store_true")
args = parser.parse_args()

for s in generate(args.max_count, args.max_length, args.const_count, args.const_length):
    print(s)
