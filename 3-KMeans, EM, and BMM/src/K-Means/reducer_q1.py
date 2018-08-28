#!/usr/bin/env python

import sys
import numpy as np

current_index = None

centroid = np.zeros(28*28)
num_member = 0

for line in sys.stdin:
    index, pixels = line.strip().split('\t')
    pixels = pixels.split()

    if current_index:
    	if(index == current_index):
    		for r in range(0,28):
    			for c in range(0,28):
    				centroid[r*28+c] += int(pixels[r*28+c])
    		num_member += 1
    	else:
    		w_str = 'Centroid ' + current_index + ':'
    		for i in range(0, 28*28):
    			w_str += str(centroid[i]/num_member) + " "
    		w_str = w_str[:-1]
    		w_str += "," + str(num_member) + "\n"
    		print(w_str)
    		centroid = np.zeros(28*28)
    		num_member = 0
    current_index = index

if(current_index>1):
	w_str = 'Centroid ' + str(current_index) + ':'
	for i in range(0, 28*28):
		w_str += str(centroid[i]/num_member) + " "
	w_str = w_str[:-1]
	w_str += "," + str(num_member)
	print(w_str)





