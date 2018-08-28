#!/usr/bin/env python

import numpy as np
import os
import sys

K = 10
D = 784
N = 60000

r = np.zeros(K)
pi = np.zeros(K)

current_index = None
count_score = 0

fname = 'params.txt'

for line in sys.stdin:
	line = line.strip()
	index, str_pass = line.split('\t')
	observation, score = str_pass.split(',')
	observation = observation.split()

	if (index == current_index):
		count_score += float(score)
		sum_pre = [pre+score*pixel for pre,pixel in zip(sum_pre, observation)]
	else:
		if current_index:
			pi[index] = count_score/N
			sum_pre = [x/count_score for x in sum_pre]
			print str(sum_x).lstrip('[').rstrip(']')
			current_index = index
			count_score = score
			sum_pre = [pre*score for pre in observation]

if (current_index == index):
	pi[index] = count_score/N
	sum_pre = [x/count_score for x in sum_pre]
	print str(sum_x).lstrip('[').rstrip(']')

print str(pi).lstrip('[').rstrip(']')
