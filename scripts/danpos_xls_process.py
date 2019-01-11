#!/usr/bin/env python3

# Eric Zheng
# 2018-October-24

# processes the "XLS" (really a TSV) outputted by danpos dpos to a bed graph

# assumes arguments:
# 1) path to the XLS file
# 2) path to where output should be written

import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

def outverify(path):
    level = 0
    
    if Path(path).expanduser().exists():
        level +=1
        file = Path(path).name
        raise ImportWarning(f"Warning: file already exists: {file}")
    
    return

def dirverify(path):
    
    if not Path(path).expanduser().is_dir():
        file = Path(path).name
        raise ImportError(f"FATAL: directory does not exist: {file}")
    
    return

def inverify(path):
    level = 0
    
    if not Path(path).expanduser().exists():
        level +=1
        file = Path(path).name
        raise ImportWarning(f"Warning: file does not exist: {file}")
    
    return

def fopen(path):
    # functionalize the file-opening process so I don't have issues down the line.
    return open(Path(path).expanduser(), 'wt')


# ========= Main segment =========

# verify arguments
cmd_input = sys.argv[1]
cmd_output = sys.argv[2]

inverify(cmd_input)
outverify(cmd_output)

# read in data
data = pd.read_table(cmd_input, dtype={'chr':object})

print("Peak Height summary statistics:")
print(data["smt_value"].describe())

median = data["smt_value"].median()
mean = data["smt_value"].mean()

# filter data
filtered_mean = data[data["smt_value"]>= 1.5*mean]
filtered_median = data[data["smt_value"]>= 1.5*median]

# note that I'm using 1.5x mean, but can easily change to median
data_output = filtered_mean
print("filtering peaks to those with summit height >= 1.5* mean")
print("remaining peaks: ", len(data_output))

# prepare for output
bedgraph = data_output[["chr", "start", "end", "smt_value"]]
file_output = fopen(cmd_output)
print("track type=bedGraph", file=file_output)
bedgraph.to_csv(file_output, sep = '\t', header = False, index = False, mode = 'a')
file_output.close()
