#Creates the image of the regular Block
#Updates coordinates 


import pygame
import math
import time
from GameObject import GameObject

class Block(GameObject):
    @staticmethod
    def init():
        Block.image = pygame.image.load('Block.png').convert_alpha()
        Block.image = pygame.transform.scale(Block.image,(40, 40))
        #Block image credited to
        #http://fantendo.wikia.com/wiki/File:Brick_Block.png
        
    def __init__(self, x, y):
        super(Block, self).__init__(x, y, Block.image, 2)
        self.x = x 
        self.y = y
    
    

    def update(self, screenWidth, screenHeight):
        super(Block, self).update(screenWidth, screenHeight)
