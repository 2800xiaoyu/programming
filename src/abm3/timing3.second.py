# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:03:23 2023

@author: xiaoyu
"""

import random
import matplotlib.pyplot as plt
import time
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
# n_agents = 500

# Move agents
'''
for i in range(n_agents):
    # Change agents[i] coordinate randomly
    # Change x-coordinate
    rn = random.randint(0, 99)
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
# print(agents)

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
'''

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates
    x = x1 - x0
    # Calculate the difference in the y coordinates
    y = y1 - y0
    # Return the Sum the squared differences square rooted
    return (x*x + y*y) ** 0.5
'''
max_distance = 0 # Initialise max_distance
for a in agents:
    for b in agents:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)
'''
def get_max_distance(): # Define a function that returns maximum distance between all the agents
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            # if i!= j:
            # if i < j:
                # print("i", i, "j", j)
            b = agents[i]
            distance = get_distance(a[0], b[0], a[1],b[1])
            # print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            # print("max_distance", max_distance)
    return max_distance

def get_min_distance():
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = get_distance(a[0], b[0], a[1], b[1])
            print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            print("min_distacne", min_distance)
    return min_distance

def get_max_min_distacne():
    max_distance = 0
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents), 1):
            b = agents[j]
            distance = get_distance(a[0], b[0], a[1], b[1])
            max_distance = max(max_distance, distance)
            min_distance = min(min_distance, distance)
    return max_distance, min_distance

# Create a list to store timing results
run_times = []
startr = 500
stopr = 5000
stepr = 500
for n_agents in range(startr, stopr, stepr):
    print(n_agents)
    # Create a list to store agents and initialise agents
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    # print(agents)
    
    start = time.perf_counter()
    print("Maximum distacne between all the agents", get_max_distance())
    # print("Minimum distance between all the agents", get_min_distance())
    end = time.perf_counter()
    run_time = end - start
    print("Time taken to calculate maximum distance", end - start, "seconds")
    # print("Time taken to calculate minimum distance", end - start, "seconds")
    run_times.append(run_time)

# Plot
plt.title("Time taken to calculate maximum distance for different numbers of agents")
plt.xlabel("Number of agents")
plt.ylabel("Time")
i = 0
for n_agents in range(startr, stopr, stepr):
    plt.scatter(n_agents, run_times[i], color='black')
    i = i + 1
plt.show()
'''
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
'''