import numpy as np
import matplotlib.pyplot as plt

# Added the missing parameter offset to both functions

def get_cos_x(steps, radius, offset=0):
    output = []
    for i in range(len(steps)):
        # added the offset to the result of radius * cos to move the circle on x axis
        output.append((radius * float(np.cos(steps[i])) + offset))
    return output

def get_sin_y(steps, radius, offset=0):
    output = []
    for i in range(len(steps)):
        # added the offset to the result of radius * cos to move the circle on y axis
        output.append((radius * float(np.sin(steps[i])) + offset))
    return output


if __name__ == "__main__":
    pass