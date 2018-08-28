#!/usr/bin/env python

import sys
import os
import random as rnd
import numpy as np

fname = 'centroid.txt'

centroid = np.zeros((10,5,5))

def distance(pt1,cen_num):
    dist = 0
    for r in range(0, 5):
        for c in range(0, 5):
            dist += (float(pt1[r*5+c]) - centroid[cen_num][r][c]) * (float(pt1[r*5+c]) - centroid[cen_num][r][c])
    return dist

if os.path.exists(fname):
        if os.path.getsize(fname) == 0:
            with open(fname,"a") as f:
                for o in range(0,10):
                    w_str = 'Centroid ' + str(o) + ':'
                    for k in range(0, 5*5):
                        w_str += str(rnd.randint(0,255)) + ' '
                    w_str = w_str[:-1]
                    w_str += ',0\n'
                    f.write(w_str)
            f.close()
            exit()


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

for line in sys.stdin:
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

    str_pass = ""
    for pixel in pixels:
        str_pass = str_pass + str(pixel) + " "
    str_pass = str_pass[:-1]

    print '%s\t%s' % (str(close_index), str_pass)