#!/usr/bin/env python

import sys
import copy

wordfreq = {}
pairfreq = {}
temp = {}

num_lines = 0
threshold = 0.005
top_num = 40
fname = './shakespeare_basket/shakespeare_basket3'

# Count the freq of each words
with open(fname) as f:
    lines = [line.rstrip('\n') for line in open(fname)]
    for line in lines:
        num_lines += 1
        words = line.split()
        words = list(set(words))
        for word in words:
            if word not in wordfreq:
                wordfreq[word] = 1
            else:
                wordfreq[word] += 1

for word in wordfreq:
    if (wordfreq[word] >= threshold * num_lines):
        temp[word] = wordfreq[word]

wordfreq = copy.deepcopy(temp)
temp = {}

# Second step of A-Priori
with open(fname) as f:
    lines = [line.rstrip('\n') for line in open(fname)]
    for line in lines:
        words = line.split()
        words = list(set(words))
        for j in range (0,len(words)-1):
            for k in range (j+1,len(words)):
                if(words[j] in wordfreq) and (words[k] in wordfreq):
                    if(words[j]<=words[k]):
                        pair = words[j]+","+words[k]
                    else:
                        pair = words[k]+","+words[j]
                    if pair not in pairfreq:
                        pairfreq[pair] = 1
                    else:
                        pairfreq[pair] += 1


if(len(pairfreq) > top_num):
    topkeys = sorted(pairfreq, key=pairfreq.get,reverse=True)[:top_num]
else:
    topkeys= sorted(pairfreq, key=pairfreq.get,reverse=False)

for topkey in topkeys:
    print(topkey,pairfreq[topkey])
