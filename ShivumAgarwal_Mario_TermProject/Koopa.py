import pygame
import math
import time
import random
from GameObject import GameObject

class Koopa(GameObject):
    @staticmethod
    def init():
        Koopa.image = pygame.image.load('Koopa.png').convert_alpha()
        Koopa.image = pygame.transform.scale(Koopa.image,(15, 25))
        Koopa.image = pygame.transform.flip(Koopa.image, True, False)
        #Koopa Image credited to
        #http://www.neoseeker.com/forums/69/t1089599-inf-gfx-3d-matte-painting/22.htm
        
        
        
    def __init__(self, x, y, bound):
        super(Koopa, self).__init__(x, y, Koopa.image, 2)
        self.x = x
        self.y = y
        self.Counter = True
        self.seconds = 3
        self.rightX = self.x + bound
        self.leftX = self.x - bound
        

        
    def deathSound(self):
        pygame.mixer.Sound("Stomp.OGG").play()

    def changeCounter(self):
        if (self.Counter == True):
            self.Counter = False
        elif (self.Counter == False):
            self.Counter = True

    def update(self, screenWidth, screenHeight):
        
        if(self.x < self.rightX and self.Counter == True):
            self.x+=1
        
        if (self.x >= self.rightX):
            self.Counter = False
    
        if (self.x > self.leftX and self.Counter == False):
            self.x -=1
        
        if (self.x <= self.leftX):
            self.Counter = True
        
        super(Koopa, self).update(screenWidth, screenHeight)

        
    def setX(self, x):
        self.x -= x
        self.rightX -= x
        self.leftX -= x


