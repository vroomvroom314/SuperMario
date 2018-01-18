import pygame
import math
import time
from GameObject import GameObject


class GameOver(GameObject):
    @staticmethod
    def init():
        GameOver.image = pygame.image.load('GameOver.png').convert_alpha()
        GameOver.image = pygame.transform.scale(GameOver.image,(800, 600))
        
        #Game Over image credited to
        #https://nohategaming.com/2017/07/super-mario-oddyssey-wont-have-a-game-over-screen/
        
    
    def __init__(self, x, y):
        super(GameOver, self).__init__(x, y, GameOver.image, 2)
        self.x = x 
        self.y = y
    
    
    def update(self, keysdown, screenWidth, screenHeight):
        super(GameOver, self).update(screenWidth, screenHeight)
       
            
            