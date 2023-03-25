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

# set the random seed
random.seed(0)

# set parameters
n_agents = 10
n_iterations = 1000     

# initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

def get_distance(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0
    #return 0.5 ** ( x*x + y*y )
    return ( x*x + y*y ) **  0.5 
# print(get_distance(0,0,3,4))

# Calculate the maximum distance
# Initialise max_distance
max_distance = 0
for a in agents:
    for b in agents:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)

def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            print("max_distance", max_distance)

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99
    
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        rn =random.random()
        # Apply movement constraints.
        if agents[i][0] < x_min:
            agents[i][0] = x_min
        if agents[i][1] < y_min:
            agents[i][1] = y_min
        if agents[i][0] > x_max:
            agents[i][0] = x_max
        if agents[i][1] > y_max:
            agents[i][1] = y_max

# Plot
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot right red
r = max(agents, key=operator.itemgetter(0))
print(r)
plt.scatter(r[0], r[1], color='red')
# Plot left yellow
l = min(agents, key=operator.itemgetter(0))
print(l)
plt.scatter(l[0], l[1], color='yellow')
# Plot top green
t = max(agents, key=operator.itemgetter(1))
print(t)
plt.scatter(t[0], t[1], color='green')
# Plot bottom pink
b = min(agents, key=operator.itemgetter(1))
print(b)
plt.scatter(b[0], b[1], color='pink')
plt.show()

start = time.perf_counter()
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "second")