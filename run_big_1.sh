SOURCE_BASE_PATH="$HOME/task"
echo $SOURCE_BASE_PATH

INPUT_DIR="/task/output_big"
OUTPUT_DIR="/task/output_big_1"

HADOOP_STREAMING_PATH="/usr/lib/hadoop-mapreduce/hadoop-streaming.jar"

hdfs dfs -rm -r $INPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR

hdfs dfs -mkdir -p $INPUT_DIR
hdfs dfs -copyFromLocal $SOURCE_BASE_PATH/data/output_big $INPUT_DIR

chmod 0777 $SOURCE_BASE_PATH/src/mapper_1.py
chmod 0777 $SOURCE_BASE_PATH/src/reducer_1.py

hadoop_streaming_arguments="\
	-file $SOURCE_BASE_PATH/src/mapper_1.py -mapper mapper_1.py \
	-file $SOURCE_BASE_PATH/src/reducer_1.py -reducer reducer_1.py \
	-file $SOURCE_BASE_PATH/data/input/ratings.dat \
	-input $INPUT_DIR/* -output $OUTPUT_DIR \
	"

hadoop jar $HADOOP_STREAMING_PATH $hadoop_streaming_arguments

hdfs dfs -copyToLocal $OUTPUT_DIR $SOURCE_BASE_PATH/data

hdfs dfs -rm -r $INPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR
