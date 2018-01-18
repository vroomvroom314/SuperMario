import pygame
import math
import time
from GameObject import GameObject


class TitleScreen(GameObject):
    @staticmethod
    def init():
        TitleScreen.image = pygame.image.load('Title.png').convert_alpha()
        TitleScreen.image = pygame.transform.scale(TitleScreen.image,(800, 600))
        #Title Screen image Credited to 
        #http://www.playbuzz.com/friendlyfunp10/normal-mode-mario-trivia
        #https://wall.alphacoders.com/big.php?i=445906
    
    def __init__(self, x, y):
        super(TitleScreen, self).__init__(x, y, TitleScreen.image, 2)
        self.x = x 
        self.y = y
    
    
    def update(self, keysdown, screenWidth, screenHeight):
        super(TitleScreen, self).update(screenWidth, screenHeight)
       
            
            