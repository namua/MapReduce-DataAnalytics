#!/usr/bin/env python

from operator import itemgetter
import sys

#size_dataset = 1000
fid_m = None
old_fid_m = None
current_key = None

sim_arr = {}
id_list = {}
checksum_arr = {}

#for i in range(size_dataset):
#	sim_arr.append(0)
#	checksum_arr.append(0);
#	id_list.append("");

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    fid_m, other = line.split('\t')
    fid_s, pid = other.split(',')

    #m_id = fid_m

    if(current_key == fid_m):
        if(sim_arr.get(int(fid_s)) == None):
            sim_arr[int(fid_s)] = 1
        else:
            sim_arr[int(fid_s)] += 1

        if(checksum_arr.get(int(fid_s)) == None):
            checksum_arr[int(fid_s)] = int(pid)
        else:
            checksum_arr[int(fid_s)] += int(pid)

        if(id_list.get(int(fid_s)) == None):
            id_list[int(fid_s)] = pid
            id_list[int(fid_s)] += ","
        else:
            id_list[int(fid_s)] += pid
            id_list[int(fid_s)] += ","

        old_fid_m = fid_m

    else: 
        if (current_key != None):
            top_1 = -1
            top_2 = -1
            top_3 = -1

            sim_arr[-1] = -1

            keylist = sim_arr.keys()

            for key in keylist:
                if(sim_arr[key] >= sim_arr[top_1]):
                    top_3 = top_2
                    top_2 = top_1
                    top_1 = key
                elif(sim_arr[key] >= sim_arr[top_2]):
                    top_3 = top_2
                    top_2 = key
                elif(sim_arr[key] >= sim_arr[top_3]):
                    top_3 = key

            final = [top_1, top_2, top_3]

            if(old_fid_m != None):
                out_m = old_fid_m
                old_fid_m = fid_m
            else:
                out_m = fid_m
                old_fid_m = fid_m

            for j in range(3):
                if(final[j] != -1):
                    output_str = str(out_m) + ":"
                    output_str += str(final[j]) + ","
                    output_str += "{"
                    output_str += id_list[final[j]]
                    output_str = output_str[:len(output_str)-1]
                    output_str += "}"
                    output_str += ","
                    output_str += str(checksum_arr[final[j]])
                    print(output_str)

            sim_arr = {}
            checksum_arr = {}
            id_list = {}

            sim_arr[int(fid_s)] = 1
            checksum_arr[int(fid_s)] = int(pid)
            id_list[int(fid_s)] = pid
            id_list[int(fid_s)] += ","

        else:
            sim_arr[int(fid_s)] = 1
            checksum_arr[int(fid_s)] = int(pid)
            id_list[int(fid_s)] = pid
            id_list[int(fid_s)] += ","

        current_key = fid_m


if(current_key == fid_m):
    top_1 = -1
    top_2 = -1
    top_3 = -1

    sim_arr[-1] = -1

    keylist = sim_arr.keys()

    for key in keylist:
        if(sim_arr[key] > sim_arr[top_1]):
            top_3 = top_2
            top_2 = top_1
            top_1 = key
        elif(sim_arr[key] > sim_arr[top_2]):
            top_3 = top_2
            top_2 = key
        elif(sim_arr[key] > sim_arr[top_3]):
            top_3 = key

    final = [top_1, top_2, top_3]

    for j in range(3):
        if(final[j] != -1):
            output_str = str(fid_m) + ":"
            output_str += str(final[j]) + ","
            output_str += "{"
            output_str += id_list[final[j]]
            output_str = output_str[:len(output_str)-1]
            output_str += "}"
            output_str += ","
            output_str += str(checksum_arr[final[j]])
            print(output_str)

# do not forget to output the last word if needed!
