# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:05:29 2023

@author: xiaoyu
"""

import random
import matplotlib
from matplotlib import pyplot as plt
import operator
import time
import my_modules.agentframework as af
import my_modules.io as io

# read_data function in io
environment, n_rows, n_cols = io.read_data()

# set the random seed
random.seed(0)

# set parameters
n_agents = 10   

# initialise agents
agents = []
for i in range(n_agents):
    # create an agent
    agents.append(af.Agent(i, environment, n_cols, n_rows))
    print(agents[i])
print(agents)

def get_distance(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0
    #return 0.5 ** ( x*x + y*y )
    return ( x*x + y*y ) **  0.5 
# print(get_distance(0,0,3,4))

# Calculate the maximum distance
# Initialise max_distance
def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents)):
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
            print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            print("max_distance", max_distance)

max_distance = 0
for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
        distance = get_distance(a.x, a.y, b.x, b.y)
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)
        
# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum an agents x coordinate is allowed to be.
x_max = n_cols - 1
# The maximum an agents y coordinate is allowed to be.
y_max = n_rows - 1

# Move agents    
n_iterations = 100
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        # Change agents(i) coordinates randomly
        agents[i].move(x_min, y_min, x_max, y_max)

# Plot
plt.imshow(environment)
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')

plt.show()

start = time.perf_counter()
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "second")