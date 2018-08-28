hdfs dfs -mkdir /user/jj015/input_l
hdfs dfs -put ./Large.txt /user/jj015/input_l

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapreduce.map.memory.mb=4096 -D mapreduce.reduce.memory.mb=4096 -D mapred.map.tasks=40 -D mapred.reduce.tasks=10 -file mapper-yc.py -mapper mapper-yc.py -file reducer-yc.py -reducer reducer-yc.py -input /user/jj015/input_l/* -output output_l

hdfs dfs -cat /user/jj015/output_l/* > out_l.txt
hdfs dfs -rmr /user/jj015/output_l