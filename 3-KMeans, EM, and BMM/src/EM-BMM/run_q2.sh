#!/bin/bash
chmod +x mapper_q2.py reducer_q2.py

for i in `seq 1 1`;
do
	hdfs dfs -rm -r /user/ly116/output_q2

	hdfs dfs -mkdir /user/ly116/bin_train
	hdfs dfs -put ./dataset/bin_train.txt /user/ly116/bin_train

	hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-D mapreduce.map.memory.mb=8192 \
	-D mapreduce.reduce.memory.mb=4096 \
	-D mapred.map.tasks=10\
	-D mapred.reduce.tasks=1 \
	-input /user/ly116/bin_train/* \
	-output output_q2 \
	-file mapper_q2.py -mapper mapper_q2.py \
	-file reducer_q2.py -reducer reducer_q2.py \
	-file params.txt

	hdfs dfs -cat /user/ly116/output_q2/* > params_new.txt

	cat params_new.txt > params.txt
	cat params_new.txt >> param_all.txt

	hdfs dfs -rm -r /user/ly116/output_q2
done
