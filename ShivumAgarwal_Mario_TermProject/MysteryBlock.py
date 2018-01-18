import pygame
import math
import time
from GameObject import GameObject

class MysteryBlock(GameObject):
    @staticmethod
    def init():
        MysteryBlock.image = pygame.image.load('Mblock.png').convert_alpha()
        MysteryBlock.image = pygame.transform.scale(MysteryBlock.image,(40, 40))
    
        
    def __init__(self, x, y):
        super(MysteryBlock, self).__init__(x, y, MysteryBlock.image, 2)
        self.x = x 
        self.y = y
        
    

    def update(self, screenWidth, screenHeight):
        super(MysteryBlock, self).update(screenWidth, screenHeight)
