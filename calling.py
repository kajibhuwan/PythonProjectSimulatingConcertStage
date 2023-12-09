from lights import Lights
from background import Backdrop
import numpy as np
import matplotlib.pyplot as plt
from smokemachine import Smokemachine
from props import MovingObject
import matplotlib.pyplot as plt

def main(create_lights,create_smoke_machines,create_props):

 width = 800
 height = 600

 lights=[
    Lights("purple", (10,50),np.radians(270),25,25),
    Lights("yellow", (20,50),np.radians(270),25,25),
    Lights("red", (30,50),np.radians(270),25,25),
    Lights("grey", (40,50),np.radians(270),25,25),
   
 ]
 
 smokeMachines = [Smokemachine((10,5), 'up',6, 5,'white'),
                     Smokemachine((25,5),'right',6, 5,'white'),
                     Smokemachine((40,5),'up',5, 8,'red')]
 

 
 object = MovingObject((23, 20), 3.5, 4.5, 'blue', 'red')
  

 fig,ax = plt.subplots()
 ax.set_aspect('equal')

 ax.set_xlim([0,50])
 ax.set_ylim([0,50])

 for light in lights:  
  light.calculate_light_cone(ax)
   
 for i in range(100):
   object.move(20)
   object.draw(ax)
               
 bd= Backdrop("black", "/Users/Lenovo/Desktop/Folder for Python Prac/FOP_Assignment_21376180/image.png")
 bd.set_backdrop(ax)
   
 for sm in smokeMachines:
    sm.diffuse_smoke(ax)
   
 plt.pause(0.1)
     
 plt.title("Mythical Rock Band Spinal Tap")
 plt.show()


if __name__ == "__main__":
   main(1,2,3)

   
   






