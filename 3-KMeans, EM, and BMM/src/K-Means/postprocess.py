#!/usr/bin/env python

import sys
import os
import random as rnd
import numpy as np

th = 0.05
fname = 'centroid.txt'
sname = './dataset/pca_test.txt'
wname = 'acc.txt'

centroid = np.zeros((10,5,5))

dist_store = {}

def distance(pt1,cen_num):
    dist = 0
    for r in range(0, 5):
        for c in range(0, 5):
            dist += (int(pt1[r*5+c]) - centroid[cen_num][r][c]) * (int(pt1[r*5+c]) - centroid[cen_num][r][c])
    return dist

with open(fname) as f:
    lines = [line.rstrip('\n') for line in open(fname)]
    for line in lines:
        line = line.strip()
        line, count = line.split(',')
        header, cents = line.split(':')
        header, index = header.split()
        cents = cents.split()
        for r in range(0,5):
            for c in range(0,5):
                tot = r * 5 + c
                if(tot % 2 == 0):
                    centroid[int(index)][r][c] = float(cents[tot])
                else:
                    centroid[int(index)][r][c] = float(cents[tot])

for i in range(0,10):
    dist_store[i] = []

which_line = 0

with open(sname) as s:
    lines = [line.rstrip('\n') for line in open(sname)]
    for line in lines:
        line = line.strip()
        header, line = line.split(':')
        header, digit = header.split()
        pixels = line.split()

        close_distance = distance(pixels,0)
        close_index = 0
        for i in range(1,10):
            new_dist = distance(pixels,i)
            if(close_distance > new_dist):
                close_distance = new_dist
                close_index = i
        dist_store[close_index].append(tuple((close_distance,int(digit))))
        which_line+=1
        print(which_line)

with open(wname,'w') as w:
    for i in range(0,10):
        temp = []
        dist_store[i].sort(key=lambda tup: tup[0])
        for k in range(0,int(len(dist_store[i])*th)):
            temp.append(dist_store[i][k])

        index_count = [0] * 10
        for tup in temp:
            index_count[tup[1]] += 1
        final_index = index_count.index(max(index_count))
        pos_count = 0
        tot_count = 0
        for tup in dist_store[i]:
                if(tup[1] == final_index):
                    pos_count += 1
                tot_count += 1
        str_out = 'Cluster Number ' + str(i) + ':' + str(len(dist_store[i])) + ',' + str(int(len(dist_store[i]) * th)) + ',' + str(final_index) + ',' + str(pos_count) + ',' + str(pos_count/tot_count) + '\n'
        w.write(str_out)

        