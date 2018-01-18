#Handles all properties related to the Mario Object
#Handles player movement and player gravity physics

import pygame
import math
import time
from GameObject import GameObject
vec = pygame.math.Vector2

class Ship(GameObject):
   
    def __init__(self, x, y,image):
        super(Ship, self).__init__(x,y, image, 30)
        self.base = y
        self.power = 1
        self.drag = 0.9
        self.angleSpeed = 5
        self.angle = 0  # starts pointing straight up
        self.maxSpeed = 30
        self.inAir = False
        self.walking = False
        self.lastupdate = 0
        self.currentFrame = 0
        self.x = x
        self.y = y 
        self.rvx = 3
        self.lvx = 3
        self.lives = 3
    
    
    def getAir(self):
        return self.inAir
    
    def jump(self):
        pygame.mixer.Sound("Jump.OGG").play()
    
    def setAir(self, val):
        self.inAir = val
    
    
    def Move(self, x, y):
        self.x = x
        self.y = y
    
        
    def stopMoving(self, keysDown, direction):
        if direction == True:
            self.lvx = 0
        elif direction == False:
            self.rvx = 0
            
    def die(self):
        pygame.mixer.Sound("LoseLife.OGG").play()
        self.lives -= 1
    
    def getLives(self):
        return self.lives
    
    
    def deadAction(self):
       
        while (self.y > 0):
            self.y -= 15

   
    def startMoving(self, keysDown):
        self.rvx = 3
        self.lvx = 3
    
    def moveUp(self):
        self.y-=15
        self.inAir = False
        
    def update(self, keysDown, screenWidth, screenHeight):

      
        if keysDown(pygame.K_LEFT):
            self.x-=self.lvx
            self.walking = True

            
        
        
        if keysDown(pygame.K_RIGHT):
            self.x+=self.rvx
            self.walking = True


        
        
        if keysDown(pygame.K_UP) and self.inAir == False:
                self.inAir = True
                self.thrust(self.power*70)
                Ship.jump(self)
                
            
       
        else:
            vx, vy = self.velocity
            self.velocity = self.drag * vx, self.drag * vy
            if (self.inAir == True):
                self.y+=7
             
                    
            
        
        
        super(Ship, self).update(screenWidth, screenHeight)
        #print(self.x, self.y)

    def fall(self):
            self.newDrag = 0.5
            vx, vy = self.velocity
            self.velocity = self.newDrag * vx, self.newDrag * vy
            if (self.inAir == True):
                #self.fall(self.power)
                self.y+=7
                if (self.y >= self.base):
                    self.inAir = False
    
    
    def thrust(self, power):
        angle = math.radians(self.angle)
        vx, vy = self.velocity
        # distribute the thrust in x and y directions based on angle
        vy -= power * math.sin(angle+90)
        speed = math.sqrt(vx ** 2 + vy ** 2)
        if speed > self.maxSpeed:
            factor = self.maxSpeed / speed
            vx *= factor
            vy *= factor
        self.velocity = (vx, vy)
   

            



