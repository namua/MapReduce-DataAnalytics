#!/usr/bin/env python

import sys

current_pair = None
for line in sys.stdin:
    pair,count = line.strip().split('\t')
    if pair == current_pair:
        continue
    else:
        if current_pair:
            print current_pair
        current_pair = pair
if current_pair == pair:
    print current_pair
