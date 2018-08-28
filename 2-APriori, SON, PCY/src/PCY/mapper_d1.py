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
hashtable = [0 for x in range(100000)]

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

    for j in range(0, len(words)-1):
        for k in range(j+1, len(words)):
            hash_val = hash(words[j] + words[k]) % 100000
            hashtable[hash_val] += 1

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
                    hash_val = hash(word_basket[j] + word_basket[k]) % 100000
                    if(hashtable[hash_val] >= threshold * num_lines / p):
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
