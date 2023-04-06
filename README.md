# programming
https://github.com/2800xiaoyu/programming/edit/main/README.md

# Introduction
The ABM is a kind of useful model for studying behaviour and emergency in complex systems.
The model uses 'agent' to represent doing various things in simulation steps.
What the agents do will in some ways change their characteristics, the characteristics of other agents, and the spatial 'environment' in which they are located and which is represented as a different kind of entity.

# abm1 & abm2
In these two parts, the main mission are:
1. create an agent list to represent a series of [x, y] coordinates.
2. using simple loops and plotting to reveal locations of points that situate in the agent.

# abm3
1. Calculate the maximum distance between two random points in the agent by defining functions (max_distance)
2. Plotting time taken to calculate maximum distance for different numbers of agents
3. Create a new loop for moving agents

# abm4
This part aims at using class in Python. Create methods in the new class like __init__() in agentframework.py.
Connect agentframework.py with model.py by using import.
Compared with former part result, the new plot is the same as it.

# abm5
Import environment and make interactions in it.
In agentframework.py:
def move(): for changing [x,y] coordinates randomly
def eat(): First, check values in environment where agents is located.
           Second, if the value is larger than 10, it reduced by 10.
                   Else, attribute of 'store' is added by 10.
Overall, it is an interaction running between 'environment' where agents is located and 'store'.
Due to the changing value is 10, the total resource of the interaction would not change.
After interaction, plotting 'environment' is achieved by matplotlib in Python.

For sixth part (Code Review and Looking Forward),
consider what happens when two or more agents are at the same location and there is less resource at the location for all the agents to have 10.
Those agents processed sooner will get to eat more resource during interaction, while total resource is unchangeable.
And, if agents are always processed in the same order, then these agents gaining more store.

# abm6
In this part, another interaction is created in agentframework.py.
In agentframework.py:
def share(): First, calculate the distance between [x, y] in agents and [self.x, self.y] in 'share'.
             Second, if the distance is smaller than neighbourhood, which is the index passed into share(),
                     then the index of agent will be stored into 'neighbourhood' list.
             Finally,the attribute 'self.store' is then divided into 'shares' and added to the 'store_shares' attribute of all the agents with indexes in 'neighbours'.
In model.py, there is another mission of this part. Create an animation GIF by using 'imageio' and output the results into a file.

# abm7
The main practical for this part is animation.

# abm8
The main practical for this part is developing a simple Graphical User Interface (GUI).

# abm9
The main practical ofr this part is importing data from an HTML to create an animation.
