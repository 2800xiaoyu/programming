# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:29:50 2023

@author: xiaoyu
"""
import random
import geometry1

class Agent():
    pass

    def __init__(self, agents, i, environment, n_rows, n_cols, x = None, y = None):
        """
        The constructor method.
        
        Parameters
        ----------
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.
        x : Integer
            For initialising the x coordinate of the agent.
        y : Integer
            For initialising the y coordinate of the agent.
        
        Returns
        -------
        None.
        
        """
        self.agents = agents
        self.i = i
        self.environment = environment
        if x == None:
            tnc = int(n_cols / 3)
            self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        else:
            self.x = x
        if y == None:
            tnr = int(n_rows / 3)
            self.y = random.randint(tnc - 1, (2 * tnr) - 1)
        else:
            self.y = y
        self.store = random.randint(0, 99)
        self.store_shares = 0
    
    def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) \
            + ", y=" + str(self.y) + ", i=" + str(self.i) + ")"
    
    def __repr__(self):
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        rn = random.randint(0, 99)
        if rn < 55:
            self.x = self.x + 2
        else:
            self.x = self.x - 2
        # Change y-coordinate
        rn = random.randint(0, 99)
        if rn > 55:
            self.y = self.y - 2
        else:
            self.y = self.y + 2
        # Apply movement constraints
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max
    
    def eat(self):
        if self.environment[self.y][self.x] >= 100:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def share(self, neighbourhood):
        # Create a list of agents in neighbourhood
        neighbours = []
        # print(self.agents[self.i])
        for a in self.agents:
            distance = geometry1.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        # print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        # print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares