# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:03:23 2023

@author: xiaoyu
"""

import random
import matplotlib.pyplot as plt
import operator
import time
import my_modules.agentframework1 as af
import my_modules.io1 as io

# Call the 'read_data' function in io1.py
environment, n_rows, n_cols = io.read_data()

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

n_iterations = 100

# Create a list to store agents and initialise agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i, environment, n_cols, n_rows))
    print(agents[i])
print(agents)

# Variables for constraining movement
# The minimum x coordinate
x_min = 0
# The minimum y coordinate
y_min = 0
# The maximum an agents x coordinate is allowed to be
x_max = n_cols - 1
# The maximum an agents y coordinate is allowed to be
y_max = n_rows - 1

# Move agents
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        # Change agents[i] coordinate randomly
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()

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
    x = x1 - x0
    y = y1 - y0
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

# Further part            
# Define a function for adding up all the values in environment            
def sum_environment():
    sum_env = 0
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            sum_env += environment[i][j]
    return sum_env

# Define a function for adding up all the store values in all the agents
def sum_agent_stores():
    sum_as = 0
    for i in range (len(agents)):
        sum_as += agents[i].store
    return sum_as

# Print the total amount of resource
sum_as = sum_agent_stores()
print("sum_agent_stores", sum_as)
sum_e = sum_environment()
print("sum_environment", sum_e)
print("total resource", (sum_as + sum_e))

end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")

# Call write_data function in io1
n_rows = io.write_data(environment)

# Plot the agents on the environment
plt.imshow(environment)
'''
# Limit plot axes and flip y-axis back
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
'''
# Change plot limits for a closer look at the centre of environment
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)
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
