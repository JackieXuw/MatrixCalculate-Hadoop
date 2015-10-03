EXAMPLE_DIR = /user/$(USER)/matmult-dense/
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000
OUTPUT_FILE_2 = $(OUTPUT_DIR)/part-00001

HADOOP_VERSION = 2.6.0
# generally I use HADOOP_HOME, for not modifying the original makefile, I set up the HADOOP_PREFIX here
HADOOP_PREFIX = /usr/local/hadoop

TOOLLIBS_DIR=$(HADOOP_PREFIX)/share/hadoop/tools/lib/

run: inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map.py,./reduce.py \
		-mapper ./map.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) \
		-numReduceTasks 1 \
		-jobconf stream.num.map.output.key.fields=4 \
		-jobconf stream.map.output.field.separator='\t' \
		-jobconf mapreduce.partition.keypartitioner.options=-k1,3
	hdfs dfs -cat $(OUTPUT_FILE)

run-2reducers: inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
                -D mapred.reduce.tasks=2 \
		-files ./map.py,./reduce.py \
		-mapper ./map.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) 
	echo "===$(OUTPUT_FILE)==="
	hdfs dfs -cat $(OUTPUT_FILE)
	echo "===$(OUTPUT_FILE_2)==="
	hdfs dfs -cat $(OUTPUT_FILE_2)

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir $(OUTPUT_DIR)

inputs: directories
	hdfs dfs -test -e $(INPUT_DIR)/matrices \
	  || hdfs dfs -put matrices $(INPUT_DIR)/matrices

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -r -f $(EXAMPLE_DIR)
	rm matrices

.PHONY: directories inputs clean run run-2reducers
