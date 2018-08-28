#!/usr/bin/env python

import sys

pairfreq = {}

threshold = 0.005
p = 1
num_lines = 4340061

current_pair = None
for line in sys.stdin:
    pair,count = line.strip().split("\t")
    count = int(count)
    if current_pair == pair:
        total += count
    else:
        if current_pair:
            if total >= num_lines * threshold / p:
                print current_pair+"\t"+str(total)
        current_pair = pair
        total = count