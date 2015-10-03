EXAMPLE_DIR = /user/$(USER)/matmult-dense/
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000

HADOOP_VERSION = 2.6.0
# generally I use HADOOP_HOME, for not modifying the original makefile, I set up the HADOOP_PREFIX here
HADOOP_PREFIX = /usr/local/hadoop

TOOLLIBS_DIR=$(HADOOP_PREFIX)/share/hadoop/tools/lib/

local: matrices map1.py map2.py reduce1.py reduce2.py
	cat matrices | ./map1.py | sort -k1,5 | ./reduce1.py | ./map2.py | sort -k1,2 | ./reduce2.py

matrices: generateDense.py
	./generateDense.py


run: inputs
	hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map1.py,./reduce1.py \
		-mapper ./map1.py \
		-reducer ./reduce1.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) \
		-numReduceTasks 1 \
		-jobconf stream.num.map.output.key.fields=5 \
		-jobconf stream.map.output.field.separator='\t' \
		-jobconf mapreduce.partition.keypartitioner.options=-k1,3
	hdfs dfs -rm $(INPUT_DIR)/part-00000
	hdfs dfs -mv $(OUTPUT_FILE) $(INPUT_DIR)/part-00000
	hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map2.py,./reduce2.py \
		-mapper ./map2.py \
		-reducer ./reduce2.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) \
		-numReduceTasks 1 \
		-jobconf stream.num.map.output.key.fields=2 \
		-jobconf stream.map.output.field.separator='\t'
	hdfs dfs -cat $(OUTPUT_FILE)

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir $(OUTPUT_DIR)

inputs: directories matrices
	hdfs dfs -rm $(INPUT_DIR)/part-00000
	hdfs dfs -put matrices $(INPUT_DIR)/part-00000

clean:
	hdfs dfs -rm -f -r $(INPUT_DIR)
	hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hdfs dfs -rm -r -f $(EXAMPLE_DIR)
	rm matrices

.PHONY: directories inputs clean run run-2reducers local
