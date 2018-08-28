#!/usr/bin/env python

import sys
import os
import random as rnd
import numpy as np

total_pts = 50000
N_comp = 25
N_cluster = 10

fname = 'centroid.txt'
wname = 'GMM_result.txt'
sname = './dataset/pca_train.txt'

centroid = np.zeros((N_cluster,N_comp))

cluster_store = {}
cov_store = {}
weight_store = {}

# All indices are based on the centroid matrix
def distance(pt1,cen_num):
    dist = 0
    for i in range(0,N_comp):
        dist += (float(pt1[i]) - centroid[cen_num][i]) * (float(pt1[i]) - centroid[cen_num][i])
    return dist

with open(fname) as f:
    lines = [line.rstrip('\n') for line in open(fname)]
    for line in lines:
        line = line.strip()
        line, count = line.split(',')
        header, cents = line.split(':')
        header, index = header.split()
        cents = cents.split()

        cluster_store[int(float(index))] = np.zeros((int(count),N_comp))
        weight_store[int(float(index))] = int(count) / total_pts

        for i in range(0,N_comp):
            centroid[int(float(index))][i] = float(cents[i])

count = np.zeros(10)

with open(sname) as s:
    lines = [line.rstrip('\n') for line in open(sname)]
    for line in lines:
        line = line.strip()
        header, line = line.split(':')
        header, digit = header.split()
        pixels = line.split()

        if(len(pixels)!=0):
            close_distance = distance(pixels,0)
            close_index = 0

            for i in range(1,N_cluster):
                new_dist = distance(pixels,i)
                if(close_distance > new_dist):
                    close_distance = new_dist
                    close_index = i
            
            for m in range(0,N_comp):  
                this_cluster_count = int(count[close_index])
                cluster_store[close_index][this_cluster_count][m] = float(pixels[m])

            count[close_index] += 1


with open(wname,'w') as w:  
    for i in range(0,N_cluster):
        out_str = "mu:"
        for k in range(0, N_comp):
            out_str += str(centroid[i][k]) + " "
        out_str = out_str[:-1] + "\n"
        w.write(out_str)

        cov_store[i] = np.cov(cluster_store[i])

        print(i)

        w.write("cov:")
        for m in range(0, np.shape(cov_store[i])[0]):
            for c in range(0, np.shape(cov_store[i])[1]):
                if(c == np.shape(cov_store[i])[0] - 1):
                    w.write(str(cov_store[i][m][c]))
                else:
                    w.write(str(cov_store[i][m][c]) + " ")
            w.write("\n")

        w.write("weight:")
        out_str = ""
        for r in range(0, N_cluster):
            out_str += str(weight_store[r]) + " "
        out_str = out_str[:-1] + "\n"
        w.write(out_str)



        