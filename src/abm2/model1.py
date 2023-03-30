# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:03:23 2023

@author: xiaoyu
"""

import random
import matplotlib.pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

# Create a list to store agents and initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)]) # Append to list agents
print(agents)

'''
# Initialise variable x0
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)
agents.append([x0, y0])
'''

# Move agents
for i in range(n_agents):
    # Change agents[i] coordinate randomly
    # Change x-coordinate
    rn = random.randint(0, 99)
    # print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 5
    else:
        agents[i][0] = agents[i][0] - 5
    # Change y-coordinate
    rn = random.randint(0, 99)
    if rn > 0.5:
        agents[i][1] = agents[i][1] - 5
    else:
        agents[i][1] = agents[i][1] + 5
print(agents)

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

# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()