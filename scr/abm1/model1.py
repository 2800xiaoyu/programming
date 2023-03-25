# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:45:31 2023

@author: xiaoyu
"""

import random

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x0 = x0 + 5
else:
    x0 = x0 - 5
print("x0", x0)

rn = random.random()
print("rn", rn)
if rn > 0.5:
    y0 = y0 - 5
else:
    y0 = y0 + 5
print("y0", y0)

# Initialise variable x1
x1 = random.randint(0, 99)
print("x1", x1)
# Initialise variable y1
y1 = random.randint(0, 99)
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
print("rn", rn)
if rn > 0.5:
    x1 = x1 - 5
else:
    x1 = x1 + 5
print("x1", x1)

rn = random.random()
print("rn", rn)
if rn < 0.5:
    y1 = y1 + 5
else:
    y1 = y1 - 5
print("y1", y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates
a = x1 - x0
# Claculate the difference in the y coordinates
b = y1 - y0
# Square the differences and add the squares
c = a*a + b*b
# Calculate the square root
distance = c ** 0.5
print("distance", distance)