#!/usr/bin/env python

import sys
import copy

wordfreq = {}
pairfreq = {}
temp = {}

basket = []

p = 1
num_lines = 0
threshold = 0.005

for line in sys.stdin:
    num_lines += 1
    line = line.strip()

    basket.append(line)

    words = line.split()
    words = list(set(words))
    for word in words:
        if word not in wordfreq:
            wordfreq[word] = 1
        else:
            wordfreq[word] += 1

for word in wordfreq:
    if (wordfreq[word] >= threshold * num_lines / p):
        temp[word] = wordfreq[word]

wordfreq = copy.deepcopy(temp)
temp = {}

for i in range (0,len(basket)):
    line = basket[i]
    word_basket = line.strip().split()
    word_basket = list(set(word_basket))
    for j in range (0, len(word_basket)-1):
        for k in range(j+1,len(word_basket)):
            if(word_basket[j] in wordfreq):
                if(word_basket[k] in wordfreq):
                    if(word_basket[j]<= word_basket[k]):
                        pair = word_basket[j]+","+ word_basket[k]
                    else:
                        pair = word_basket[k]+","+ word_basket[j]
                    if pair not in pairfreq:
                        pairfreq[pair] = 1
                    else:
                        pairfreq[pair] += 1

for pair in pairfreq:
     if (pairfreq[pair] >= threshold * num_lines / p):
        print '%s\t%s' % (pair, str(pairfreq[pair]))
