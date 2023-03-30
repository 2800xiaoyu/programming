# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:54:15 2023

@author: xiaoyu
"""

import random
import matplotlib.pyplot as plt
import time

def do(n_agents):
    random.seed(0)

    # create a list called 'agents'
    agents = []

    # create 3 random points in the agents list ([49, 97], [53, 5], [33, 65])
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])

    # calculate the maximum distance
    max_d = get_max_distance(agents)
    print("maxd", max_d)
    
    
    # create function to calculate distance between two random points
def get_distance(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0
    distance = (x*x + y*y) ** 0.5
    return distance

# create function to calculate the max distance between two random points
def get_max_distance(agents):
    # calculate the max distance between two any two points
    max_distance = 0
    # range(len(agents)) means range = [0,1,2]
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            if i < j:
                print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], b[0], a[1], b[1])
            max_distance = max(max_distance, distance)
    return max_distance

# create a list to store timing results
run_times = []
startr = 500
stopr = 5000
stepr = 500
#for n_agents in range(500, 5001, 500):
for n_agents in range(startr, stopr, stepr):
    print(n_agents)
    start = time.perf_counter()
    do(n_agents)
    end = time.perf_counter()
    print("Time taken to calculate maximum distance", end-start, "second")
    run_times.append(end-start)
 
# create a plot of times
plt.title("Time taken to calculate maximum distance for different numbers of agents")
plt.xlabel("Number of agents")
plt.ylabel("Time")
i = 0
for n_agents in range(startr, stopr, stepr):
    plt.scatter(n_agents, run_times[i], color='black')
    i = i + 1    
plt.show()