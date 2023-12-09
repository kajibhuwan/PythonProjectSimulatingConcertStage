import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from matplotlib.patches import Circle
#from matplotlib.patches import Wedge

class Smokemachine:
    def __init__(self, position, direction, intensity, neighborhood, color):
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.neighborhood = neighborhood
        self.color = color 

    def diffuse_smoke(self, ax):
        x = self.position[0]
        y = self.position[1]
        #Implementation of Van-NeuMann
        x_vec = [self.position[0]]
        y_vec = [self.position[1]]

        if self.direction == 'up':
            dx, dy = 0, 0.5
        elif self.direction == 'down':
            dx, dy = 0, -0.5
        elif self.direction == 'left':
            dx, dy = -0.5, 0
        elif self.direction == 'right':
            dx, dy = 0.5, 0

        for _ in range(self.intensity * 800):
            x += dx
            y += dy

            x_vec.append(x)
            y_vec.append(y)

        ax.scatter(x_vec, y_vec, color=self.color, alpha=1, s=0.7)
        smoke_source = Circle(self.position, 0.5, facecolor='black')
        ax.add_patch(smoke_source)
        
    