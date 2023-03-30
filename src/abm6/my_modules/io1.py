# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:32:16 2023

@author: xiaoyu
"""

import csv

def read_data():

    # Read input data
    f = open('C:/Users/xiaoyu/programming/data/input/in (2).txt', newline='')
    data = []
    
    n_rows = 0
    n_cols = None
    
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            # Print(value)
        if n_cols is None:
            n_cols = len(row)
        assert(n_cols == len(row))
        data.append(row)
        n_rows += 1
    f.close()
    return data, n_rows, n_cols

def write_data(environment):
    f = open('C:/Users/xiaoyu/programming/data/output/out.txt', 'w', newline='')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        writer.writerow(row)