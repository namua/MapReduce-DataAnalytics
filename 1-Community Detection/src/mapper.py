#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    fids = line.split()
    pid, fids[0] = fids[0].split(':')
    # increase counters
    for m_index in range(0,len(fids)):
    	#for s_index in range(m_index + 1,len(fids)):
    	for s_index in range(0,len(fids)):
    		if(m_index != s_index):
    			print '%s\t%s,%s' % (fids[m_index],fids[s_index], pid)