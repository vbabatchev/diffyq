# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle) 
# functions in order to accomplish this.

import math
import matplotlib.pyplot

moon_distance = 384e6 # m


def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    for i in range(num_steps + 1):
        angle = 2 * math.pi * i / (num_steps)
        x[i, 0] = moon_distance * math.cos(angle)
        x[i, 1] = moon_distance * math.sin(angle)

    return x


x = orbit()


def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')

    
plot_me()