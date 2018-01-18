#Creates the image of the Ground block
#Updates coordinates 

import pygame
import math
import time
from GameObject import GameObject

class Ground(GameObject):
    @staticmethod
    def init():
        Ground.image = pygame.image.load('Ground.png').convert_alpha()
        Ground.image = pygame.transform.scale(Ground.image,(50, 40))
        #Ground image credited to
        #https://dribbble.com/shots/146117-Grass-n-Dirt
        
    def __init__(self, x, y):
        super(Ground, self).__init__(x, y, Ground.image, 2)

        
    

    def update(self, screenWidth, screenHeight):
        super(Ground, self).update(screenWidth, screenHeight)