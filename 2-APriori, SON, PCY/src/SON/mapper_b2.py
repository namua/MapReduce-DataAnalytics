#!/usr/bin/env python

import sys

fname = 'candidatepair_b.txt'

threshold = 0.005

pairfreq = {}

with open(fname) as f:
    lines = [line.rstrip('\n') for line in open(fname)]
    for line in lines:
        pair = line.strip()
        pairfreq[pair] = 0

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words = list(set(words))
    for j in range (0,len(words)-1):
        for k in range(j+1,len(words)):
            if(words[j]<=words[k]):
                pair = words[j]+","+words[k]
            else:
                pair = words[k]+","+words[j]
            if pair in pairfreq:
                pairfreq[pair] += 1

for pair in pairfreq:
    print '%s\t%s' % (pair, str(pairfreq[pair]))
