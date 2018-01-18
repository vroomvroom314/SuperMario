#Creates the image of the Eraser

import pygame
import math
import time
from GameObject import GameObject

class Eraser(GameObject):
    @staticmethod
    def init():
        Eraser.image = pygame.image.load('Eraser.png').convert_alpha()
        Eraser.image = pygame.transform.scale(Eraser.image,(70, 70))
        #Eraser image credited to 
        #http://www.pngall.com/eraser-png
    
        
    def __init__(self, x, y):
        super(Eraser, self).__init__(x, y, Eraser.image, 2)
        self.x = x 
        self.y = y
        
    

    def update(self, screenWidth, screenHeight):
        super(Eraser, self).update(screenWidth, screenHeight)
