#!/usr/bin/env python

import numpy as np
import os
import sys

SEED = 1155092202
PRNG = np.random.RandomState(SEED)

K = 10
D = 784

pi = np.zeros(K)
mu = np.zeros((K,D))
r = np.zeros(K)
weight = np.zeros(K)

fname = 'params.txt'

if os.path.exists(fname):
        if os.path.getsize(fname) == 0:
            with open(fname,"a") as f:
				pi = np.random.rand(K)
				mu = np.random.rand(K, D)
				out_str = ""
				for i in range(0,K):
					out_str += str(pi[i]) + " "
				out_str = out_str[:-1]
				out_str += ","
				for k in range(0,K):
					for d in range(0,D):
						out_str += str(mu[k][d]) + " "
				out_str = out_str[:-1]
				out_str += "\n"
				f.write(out_str)
				exit()

with open(fname) as f:
    lines = [line.rstrip('\n') for line in open(fname)]
    for line in lines:
    	line = line.strip()
    	str_1, str_2 = line.split(',')
    	pis = str_1.split()
    	mus = str_2.split()
    	for k in range(0,K):
			pi[k] = float(pis[k])
			for d in range(0,D):
				mu[k][d] = float(mus[k*784+d])

for line in sys.stdin:
    line = line.strip()
    header, line = line.split(':')
    header, digit = header.split()
    observation = line.split()

    for kk in range(0, K):
    	weight[kk] = pi[kk]
    	for jj in range(0, D):
    		weight[kk] *= mu[kk][jj]**int(observation[jj]) * (1-mu[kk][jj])**(1-int(observation[jj]))

	for k in range(0,K):
		if(sum(weight) != 0):
			r[k] = weight[k] / sum(weight)

	for k in range(0,K):
		str_pass = ""
		for pixel in observation:
			str_pass = str_pass + str(pixel) + " "
		str_pass = str_pass[:-1]
		str_pass += ',' + str(r[k])
    	print '%s\t%s' % (str(k), str_pass)

		




