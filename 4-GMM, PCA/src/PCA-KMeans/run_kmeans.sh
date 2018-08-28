#!/bin/bash
chmod +x mapper_kmeans.py mapper_kmeans.py centroid.txt centroid_new.txt centroid_all.txt

for i in `seq 1 10`;
do
	hdfs dfs -rm -r /user/ly116/output_pca

	hdfs dfs -mkdir /user/ly116/pca_train
	hdfs dfs -put ./dataset/pca_train.txt /user/ly116/pca_train

	hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
	-D mapreduce.map.memory.mb=2048 \
	-D mapreduce.reduce.memory.mb=1024 \
	-D mapred.map.tasks=20 \
	-D mapred.reduce.tasks=10 \
	-input /user/ly116/pca_train/* \
	-output output_pca \
	-file mapper_kmeans.py -mapper mapper_kmeans.py \
	-file reducer_kmeans.py -reducer reducer_kmeans.py \
	-file centroid.txt

	hdfs dfs -cat /user/ly116/output_pca/* > centroid_new.txt

	cat centroid_new.txt > centroid.txt
	cat centroid_new.txt >> centroid_all.txt

	hdfs dfs -rm -r /user/ly116/output_pca
done
