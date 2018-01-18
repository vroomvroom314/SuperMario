#Handles basic Shroom Properties
#Such as movement and gravity effects


import pygame
import math
import time
from GameObject import GameObject

class Shroom(GameObject):
    @staticmethod
    def init():
        Shroom.image = pygame.image.load('shroom.png').convert_alpha()
        Shroom.image = pygame.transform.scale(Shroom.image,(15, 15))
        #Shroom image credited to
        #http://www.mariomayhem.com/bowsers_blog/index.php/2014/06/30/5-things-even-the-biggest-super-mario-fan-might-not-know/
        
        
        
    def __init__(self, x, y):
        super(Shroom, self).__init__(x, y, Shroom.image, 2)
        self.x = x 
        self.y = y
        self.initY = y
        self.inAir = False
    
    def shroomMove(self):
        self.x += 1
        
    
    def setAir(self, val):
        self.inAir = val
    
    def shroomSound(self):
        pygame.mixer.Sound("Shroom.OGG").play()

    def fall(self):
        self.y += 0
    
    def getinitY(self):
        return self.initY
        

    def update(self, screenWidth, screenHeight):
        super(Shroom, self).update(screenWidth, screenHeight)
        
        if (self.inAir == True):
            self.y+=7
    
    
    
