#The superClass to all my game Objects that used for coordinate updates
#also used for changing images for animation purposes


import pygame


#Credit to pygame notes Lukas Peraza 
########
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius):
        super(GameObject, self).__init__()
        # x, y define the center of the object
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy()  # non-rotated version of image
        w, h = image.get_size()
        self.updateRect()
        self.velocity = (0, 0)
        self.angle = 0

    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, screenWidth, screenHeight):
        self.image = pygame.transform.rotate(self.baseImage, self.angle)
        vx, vy = self.velocity
        self.x += vx
        self.y += vy
        self.updateRect()
   
########    
    def changeImage(self, image):
        self.baseImage = image
  
    def setX(self, x):
        self.x -= x
        
    def getX(self):
        return self.x
    
    def setY(self, Y):
        self.y -= y
        
    def getY(self):
        return self.y