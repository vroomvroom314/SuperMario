#Creates the image of the Coin
#Updates coordinates and coin movement

import pygame
import math
import time
from GameObject import GameObject

class Coin(GameObject):
    @staticmethod
    def init():
        Coin.image = pygame.image.load('coin.png').convert_alpha()
        Coin.image = pygame.transform.scale(Coin.image,(20, 20))
        #Coin image credited to 
        #https://www.pinterest.com/pin/492862752944527793/
        
    def __init__(self, x, y):
        super(Coin, self).__init__(x, y, Coin.image, 2)
        self.x = x 
        self.y = y
        self.initY = y
    
    def coinSound(self):
        pygame.mixer.Sound("Coin.OGG").play()


    

    def coinMove(self):
        self.y -= 1

    
    def getinitY(self):
        return self.initY
        

    def update(self, screenWidth, screenHeight):
        super(Coin, self).update(screenWidth, screenHeight)
        
    
    
