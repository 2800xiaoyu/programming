# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:29:50 2023

@author: xiaoyu
"""
import random

class Agent():
    pass

class Agent:
    def __init__(self, i):
        """
        The constructor method.

         Parameters
        ----------
        i : Integer
            To be unique to each instance.

         Returns
        -------
        None.

        """
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass
    
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