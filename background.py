import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle


class Backdrop:
  def __init__(self, color, img_path = None):
    self.color = color
    self.img_path= img_path
  def set_backdrop(self,ax):
    if self.img_path != None:
      self.background_img = mpimg.imread(self.img_path)
      ax.imshow(self.background_img, extent=[0, 50, 0, 50], aspect='auto')
    else:
      ax.set_facecolor(color = self.color)
