# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:03:23 2023

@author: xiaoyu
"""

import random
import matplotlib.pyplot as plt
import operator
import my_modules.agentframework1 as af
import my_modules.io1 as io
import geometry1
import imageio
import os
import matplotlib.animation as anim
import tkinter as tk
import requests
import bs4
import matplotlib
matplotlib.use('TkAgg')

def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents)):
            b = agents[j]
            distance = geometry1.get_distance(a.x, b.x, a.y, b.y)
            # print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            # print("max_distance", max_distance)
    return max_distance

def sum_environment():
    sum_env = 0
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            sum_env += environment[i][j]
    return sum_env

def sum_agent_stores():
    sum_as = 0
    for i in range(len(agents)):
        sum_as += agents[i].store
    return sum_as

# Move agents and model loop
def update(frames):
    # Model loop
    global carry_on
    # for ite in range(n_iterations):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        # Change agents[i] coordinate randomly
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        # print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        # print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    # print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))
    
    # Stopping condition
    # Random
    if random.random() < 0.1:
        # if sum_as / n_agents > 80:
            carry_on = False
            print("stopping condition")
    
    # Plot
    global ite
    plot()
    ite = ite + 1

def gen_function():
    global ite
    ite = 0
    global carry_on # Not actually needed as we're not assigning, but clearer
    while (ite < n_iterations) & (carry_on):
        yield ite # Return control and waits next call
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        io.write_data('C:/Users/xiaoyu/programming/data/output/out7.txt', environment)
        imageio.mimsave('C:/Users/xiaoyu/programming/data/output/out7.gif', images, fps=3)
        data_written = True
        
# Plot the agents
def plot():
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
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
    global ite
    filename = 'C:/Users/xiaoyu/programming/data/output/images/image' + str(ite) + '.png'
    # filename = 'C:/Users/xiaoyu/programming/data/output/images/image' + str(ite) + '.gif
    plt.savefig(filename)
    plt.show()
    images.append(imageio.imread(filename))
    return fig

def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()
    
def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)

if __name__ == '__main__':
    # Create directory to write images to
    try:
        os.makedirs('C:/Users/xiaoyu/programming/data/output/images')
    except FileExistsError:
        print("path exists")
        
        # For storing images
    global ite
    ite = 0
    images = []
    
    environment, n_rows, n_cols = io.read_data()
    #n_cols = io.write_data(environment)

    # Set the pseudo-random seed for reproducibility
    random.seed(0)

    # A variable to store the number of agents
    n_agents = 10

    n_iterations = 100
    
    # Neighbourhood
    neighbourhood = 50

    # Create a list to store agents and initialise agents
    url = "http://agdturner.github.io/resources/abm9/data.html"
    r = requests.get(url, verify=False)
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)
    agents = []
    store_share = 0
    for i in range(n_agents):
        # Create an agent
        y = int(td_ys[i].text) + 99
        x = int(td_xs[i].text) + 99
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols, x, y))
        print(agents[i].agents[i])
    #print(agents[i])
#print(agents)

    # Variables for constraining movement
    # The minimum x coordinate
    x_min = 0
    # The minimum y coordinate
    y_min = 0
    # The maximum an agents x coordinate is allowed to be
    x_max = n_cols - 1
    # The maximum an agents y coordinate is allowed to be
    y_max = n_rows - 1

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

    max_distance = 0 # Initialise max_distance
    for a in agents:
        for b in agents:
            distance = geometry1.get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
# Animate
# Initialise fig and carry_on
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
data_written = False
# GUI
root = tk.Tk() # Main window
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_0 = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=menu_0)
menu_0.add_command(label="Run model", command=lambda: run(canvas))
menu_0.add_command(label="Write data", command=lambda: output())
menu_0.add_command(label="Exit", command=lambda: exiting())
menu_0.entryconfig("Write data", state="disabled")
# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)
tk.mainloop()