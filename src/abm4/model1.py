# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:03:23 2023

@author: xiaoyu
"""

import random
import matplotlib.pyplot as plt
import operator
import time
import agentframework1 as af

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

n_iterations = 10

# Create a list to store agents and initialise agents
# a = af.Agent()
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i))
    print(agents[i])
print(agents)
# print("type(a)", type((a)))

# Variables for constraining movement
# The minimum x coordinate
x_min = 0
# The minimum y coordinate
y_min = 0
# The maximum x coordinate
x_max = 99
# The maximum y coordinate
y_max = 99

# Move agents
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        # Change agents[i] coordinate randomly
        agents[i].move(x_min, y_min, x_max, y_max)

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

start = time.perf_counter()

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

max_distance = 0 # Initialise max_distance
for a in agents:
    for b in agents:
        distance = get_distance(a.x, a.y, b.x, b.y)
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)

def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents)):
            b = agents[i]
            distance = get_distance(a.x, b.x, a.y, b.y)
            print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            print("max_distance", max_distance)

end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")

# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.show()