#One of the endgame states if the player completes default or designed level


import pygame
import math
import time
from GameObject import GameObject


class WinScreen(GameObject):
    @staticmethod
    def init():
        WinScreen.image = pygame.image.load('WinScreen.png').convert_alpha()
        WinScreen.image = pygame.transform.scale(WinScreen.image,(800, 500))
        #Win Screen image credited to
        #http://www.wallpapersxl.com/wallpaper/2560x1600/super-mario-sharenator-bad-desktop-pixel-boxes-3144942.html
    
    def __init__(self, x, y):
        super(WinScreen, self).__init__(x, y, WinScreen.image, 2)
        self.x = x 
        self.y = y
    
    
    def update(self, keysdown, screenWidth, screenHeight):
        super(WinScreen, self).update(screenWidth, screenHeight)
       
            
            