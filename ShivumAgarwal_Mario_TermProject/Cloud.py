import pygame
import math
import time
from GameObject import GameObject

class Cloud(GameObject):
    @staticmethod
    def init():
        Cloud.image = pygame.image.load('Cloud.png').convert_alpha()
        Cloud.image = pygame.transform.scale(Cloud.image,(70, 50))

        
    def __init__(self, x, y):
        super(Cloud, self).__init__(x, y, Cloud.image, 2)

        
    

    def update(self, screenWidth, screenHeight):
        super(Cloud, self).update(screenWidth, screenHeight)