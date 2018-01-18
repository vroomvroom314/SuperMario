#Creates the image of the Pole
#Updates coordinates 

import pygame
import math
import time
from GameObject import GameObject

class Pole(GameObject):
    @staticmethod
    def init():
        Pole.image = pygame.image.load('Pole.png').convert_alpha()
        Pole.image = pygame.transform.scale(Pole.image,(60, 300))
        #Pole image credited to
        #http://www.pinsdaddy.com/mario-checkpoint_W93TksNslLzhU3Or4j4jCpvNzXqNnlXSHuT*NUq5FTo/
        
    def __init__(self, x, y):
        super(Pole, self).__init__(x, y, Pole.image, 2)
        self.x = x 
        self.y = y
        
    

    def update(self, screenWidth, screenHeight):
        super(Pole, self).update(screenWidth, screenHeight)

    def scale(self, x, y):
        Pole.image = pygame.transform.scale(Pole.image,(x, y))