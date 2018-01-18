import pygame
import math
import time
from GameObject import GameObject

class Name(GameObject):
    @staticmethod
    def init():
        Name.image = pygame.image.load('Name.png').convert_alpha()
        Name.image = pygame.transform.scale(TitleScreen.image,(1000, 600))
        
    
    def __init__(self, x, y):
        super(TitleScreen, self).__init__(x, y, TitleScreen.image, 2)
        self.x = x 
        self.y = y
    
    
    def update(self, keysdown, screenWidth, screenHeight):
        super(TitleScreen, self).update(screenWidth, screenHeight)