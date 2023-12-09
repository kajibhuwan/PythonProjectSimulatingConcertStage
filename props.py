import matplotlib.pyplot as plt
import matplotlib.patches as patches

class MovingObject:
    def __init__(self, position, radius, side_length, circle_color, triangle_color):
        self.position = position
        self.radius = radius
        self.side_length = side_length
        self.circle_color = circle_color
        self.triangle_color = triangle_color

    def move(self, dx):
        self.position = (self.position[0] + dx, self.position[1])

    def draw(self, ax):
        circle = plt.Circle(self.position, self.radius, color=self.circle_color)
        ax.add_patch(circle)

        x = self.position[0]
        y = self.position[1]
        triangle_points = [(x, y), (x + self.side_length, y), (x + self.side_length / 2, y + self.side_length)]
        triangle = patches.Polygon(triangle_points, closed=True, facecolor=self.triangle_color)
        ax.add_patch(triangle)






'''

class MovingCircle:
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color

    def move(self, dx):
        self.position = (self.position[0] + dx, self.position[1])

    def draw(self, ax):
        circle = plt.Circle(self.position, self.radius, color=self.color)
        
        ax.add_patch(circle)


'''




