# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:35:05 2023

@author: xiaoyu
"""

def get_distance(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0
    return (x*x + y*y) ** 0.5