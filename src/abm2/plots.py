# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:16:39 2023

@author: xiaoyu
"""
import random
import matplotlib
from matplotlib import pyplot as plt
import operator

# Set parameters
random.seed(0)
n_agents = 10
n_ite = 5

# Initialise agents list
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

for j in range(n_ite):

    # Move agents
    for i in range(n_agents):
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][0] = agents[i][0] + 1
        else:
            agents[i][0] = agents[i][0] - 1
        #print("x", agents[i][0])
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[i][1] = agents[i][1] + 1
        else:
            agents[i][1] = agents[i][1] - 1
        #print("y", agents[i][1])
    print(agents)

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