#!/bin/bash
chmod +x mapper_q1.py reducer_q1.py

for i in `seq 1 10`;
do
	hdfs dfs -rm -r /user/ly116/output_q1

	hdfs dfs -mkdir /user/ly116/mnist_train
	hdfs dfs -put ./dataset/mnist_train.txt /user/ly116/mnist_train

	hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-D mapreduce.map.memory.mb=2048 \
	-D mapreduce.reduce.memory.mb=1024 \
	-D mapred.map.tasks=20 \
	-D mapred.reduce.tasks=10 \
	-input /user/ly116/mnist_train/* \
	-output output_q1 \
	-file mapper_q1.py -mapper mapper_q1.py \
	-file reducer_q1.py -reducer reducer_q1.py \
	-file centroid.txt

	hdfs dfs -cat /user/ly116/output_q1/* > centroid_new.txt

	cat centroid_new.txt > centroid.txt
	cat centroid_new.txt >> centroid_all.txt

	hdfs dfs -rm -r /user/ly116/output_q1
done
