EXAMPLE_DIR = /user/$(USER)/matmult-stream/
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000
OUTPUT_FILE_2 = $(OUTPUT_DIR)/part-00001

HADOOP_VERSION = 2.6.0
# generally I use HADOOP_HOME, for not modifying the original makefile, I set up the HADOOP_PREFIX here
HADOOP_PREFIX = /usr/local/hadoop

TOOLLIBS_DIR=$(HADOOP_PREFIX)/share/hadoop/tools/lib/

# run in local mode instead of hadoop
local: map.py reduce.py
	cat ../input/part-00000 | ./map.py | sort -k1,2 | ./reduce.py

run: inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map.py,./reduce.py \
		-mapper ./map.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) \
		-numReduceTasks 1 \
		-jobconf stream.num.map.output.key.fields=2 \
		-jobconf stream.map.output.field.separator='\t'
	hdfs dfs -cat $(OUTPUT_FILE)

run-2reducers: inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
                -D mapreduce.job.reduces=2 \
		-files ./map.py,./reduce.py \
		-mapper ./map.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) \
		-jobconf stream.num.map.output.key.fields=2 \
		-jobconf stream.map.output.field.separator='\t'
	echo "===$(OUTPUT_FILE)==="
	hdfs dfs -cat $(OUTPUT_FILE)
	echo "===$(OUTPUT_FILE_2)==="
	hdfs dfs -cat $(OUTPUT_FILE_2)

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir $(OUTPUT_DIR)

inputs: directories
	hdfs dfs -test -e $(INPUT_DIR)/part-00000 \
	  || hdfs dfs -put ../input/part-00000 $(INPUT_DIR)/part-00000

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -r -f $(EXAMPLE_DIR)

.PHONY: directories inputs clean run run-2reducers
