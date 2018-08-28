#!/bin/bash
chmod +x mapper_b1.py mapper_b2.py reducer_b1.py reducer_b2.py

hdfs dfs -rm -r /user/ly116/output_b1
hdfs dfs -rm -r /user/ly116/output_b2

hdfs dfs -mkdir /user/ly116/shakespeare3
hdfs dfs -put ./shakespeare_basket/shakespeare_basket3 /user/ly116/shakespeare3

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapreduce.map.memory.mb=4096 \
-D mapreduce.reduce.memory.mb=4096 \
-D mapred.map.tasks=20 \
-D mapred.reduce.tasks=1 \
-input /user/ly116/shakespeare3/* \
-output output_b1 \
-file mapper_b1.py -mapper mapper_b1.py \
-file reducer_b1.py -reducer reducer_b1.py

hdfs dfs -getmerge output_b1 ~/candidatepair_b.txt

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapreduce.map.memory.mb=4096 \
-D mapreduce.reduce.memory.mb=4096 \
-D mapred.map.tasks=20 \
-D mapred.reduce.tasks=1 \
-input /user/ly116/shakespeare3/* \
-output output_b2 \
-file mapper_b2.py -mapper mapper_b2.py \
-file reducer_b2.py -reducer reducer_b2.py \
-file candidatepair_b.txt

hdfs dfs -cat /user/ly116/output_b2/* > out_b.txt

hdfs dfs -rm -r /user/ly116/output_b1
hdfs dfs -rm -r /user/ly116/output_b2
