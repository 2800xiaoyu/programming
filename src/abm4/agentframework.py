# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:09:00 2023

@author: xiaoyu
"""

import random

random.seed(0)
n_agents = 10

# Initialise agents
agents = []

class Agent():
    pass

    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
    
    def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) \
            + ", y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        rn =random.random()
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        #y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            self.y = self.y + 1
        else:
            self.y = self.y - 1
            
         # Apply movement constraints.
        if self.x < x_min:
         self.x = x_min
        if self.y  < y_min:
         self.y  = y_min
        if self.x > x_max:
         self.x = x_max
        if self.y  > y_max:
         self.y  = y_max
         
agents = Agent()
print(agents)