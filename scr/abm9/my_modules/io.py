# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:28:01 2023

@author: xiaoyu
"""

import csv

def read_data():
    
# Read input data
    f = open('C:/Users/xiaoyu/programming/data/input/in.txt', newline='')
    data = []
    
    n_rows = 0
    n_cols = None
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            # print(value)
        if n_cols is None:
            n_cols = len(row)
        assert(n_cols == len(row))
        data.append(row)
        n_rows += 1
    f.close()
    return data, n_rows, n_cols
    return None #this line is never executed