import numpy as np
import matplotlib.pyplot as plt
from turtle import Turtle
from create_visual_map import *
import simulation1

TurtleBot0 = Turtle()

plt.axis('off')



for message in simulation1.sim:
    TurtleBot0.add_info_to_map(message)
    plt.imshow(create_visual_map(TurtleBot0.explorer_map))
    plt.pause(0.2)
plt.pause(20)
