#Creates background image

import pygame
import math
import time
from GameObject import GameObject

class Background(GameObject):
    @staticmethod
    def init():
        Background.image = pygame.image.load('Background.png').convert_alpha()
        Background.image = pygame.transform.scale(Background.image,(800, 500))

        
    def __init__(self, x, y):
        super(Background, self).__init__(x, y, Background.image, 2)

        
    

    def update(self, screenWidth, screenHeight):
        super(Background, self).update(screenWidth, screenHeight)