SOURCE_BASE_PATH="$HOME/task"
echo $SOURCE_BASE_PATH

INPUT_DIR="/task/input"
OUTPUT_DIR="/task/output_big_2"

HADOOP_STREAMING_PATH="/usr/lib/hadoop-mapreduce/hadoop-streaming.jar"

hdfs dfs -rm -r $INPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR

hdfs dfs -mkdir -p $INPUT_DIR
hdfs dfs -copyFromLocal $SOURCE_BASE_PATH/data/input $INPUT_DIR

chmod 0777 $SOURCE_BASE_PATH/src/mapper_2.py
chmod 0777 $SOURCE_BASE_PATH/src/reducer_2.py

hadoop_streaming_arguments="\
	-file $SOURCE_BASE_PATH/src/mapper_2.py -mapper mapper_2.py \
	-file $SOURCE_BASE_PATH/src/reducer_2.py -reducer reducer_2.py \
	-input $INPUT_DIR/* -output $OUTPUT_DIR \
	-file $SOURCE_BASE_PATH/data/input/ratings.dat \
	-file $SOURCE_BASE_PATH/data/file_big \
	-file $SOURCE_BASE_PATH/data/movies.dat \
	-file $SOURCE_BASE_PATH/data/all_films_big.txt \
	"

hadoop jar $HADOOP_STREAMING_PATH $hadoop_streaming_arguments

hdfs dfs -copyToLocal $OUTPUT_DIR $SOURCE_BASE_PATH/data

hdfs dfs -rm -r $INPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR
