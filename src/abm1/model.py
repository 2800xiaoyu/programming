# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
random.seed(0)

# Initialise variable x0
x0 = 0
# Initialise variable y0
y0 = 0

# Change x0 and y0 randomly
x0 = random.random()
y0 = random.random()
if x0 > 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
if y0 > 0.5:
    y0 = y0 + 5
else:
    y0 = y0 + 1

# Initialise variable x1 and y1
x1 = 0
y1 = 0

# Change x1 and y1 randomly
x1 = random.randint(0, 99)
y1 = random.randint(0, 99)
if x1 > 55:
    x1 = x1 + 2
else:
    x1 = x1 + 3
if y1 > 55:
    y1 = y1 + 1
else:
    y1 = y1 + 5

# Calculate the difference in the x coordinates.
# Calculate the difference in the y coordinates.
# Square the differences and add the squares
# Calculate the square root
x0 = 0
y0 = 0
x1 = 3
y1 = 4
a = x1 - x0
b = y1 - y0
c = a*a + b*b
distance = c**0.5
print("diatance", distance)