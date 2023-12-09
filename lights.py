import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

class Lights:
    def __init__(self, color, position, direction, intensity, spread_angle_deg):
        self.color = color
        self.position = position
        self.direction = direction
        self.intensity = intensity
        self.spread_angle_deg = spread_angle_deg

    def calculate_light_cone(self, ax):        
        cone_angle = self.intensity * 5

        start_angle =np.degrees(self.direction) - cone_angle/12

        end_angle = np.degrees(self.direction) + cone_angle/12

        wedge = Wedge(self.position, cone_angle, start_angle, end_angle, alpha=0.5, facecolor=self.color)
        ax.add_patch(wedge)
        ax.plot(self.position[0], self.position[1], 'ro')

    
    
