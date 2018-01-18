#Creates the image of the regular Tube
#Updates coordinates 

import pygame
import math
import time
from GameObject import GameObject

class Tube(GameObject):
    @staticmethod
    def init():
        Tube.image = pygame.image.load('Tube.png').convert_alpha()
        Tube.image = pygame.transform.scale(Tube.image,(40, 60))
        #Tube image credited to
        #https://www.emaze.com/@ALTFCORZ/presentation-name
    
        
    def __init__(self, x, y):
        super(Tube, self).__init__(x, y, Tube.image, 2)
        self.x = x 
        self.y = y
        
    

    def update(self, screenWidth, screenHeight):
        super(Tube, self).update(screenWidth, screenHeight)
