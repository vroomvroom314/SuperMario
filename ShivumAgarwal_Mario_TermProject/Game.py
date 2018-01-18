#15112 Term Project 2017
#By Shivum Agarwal 
#Section G

#Handles the majority of Super Mario Bros Implementation
#Completely initializes default level and level design feature
#Handles Object interactions
#Draws all of the objects onto the screen
#Animates Mario movements
#Updates all objects

import pygame
from Ship import Ship
from pygamegame import PygameGame
from Block import Block
from Background import Background
from Cloud import Cloud
from Ground import Ground
from Koopa import Koopa
from Tube import Tube
from TitleScreen import TitleScreen
from Coin import Coin 
from MysteryBlock import MysteryBlock
from Pole import Pole
from Shroom import Shroom
from Eraser import Eraser
from GameOver import GameOver
from WinScreen import WinScreen
import random
import time


class Game(PygameGame):
    def baseVals(self):
        self.base = self.height-30
        self.start = True
        self.running = False
        self.levelDesign = False 
        self.myFont = pygame.font.SysFont("chalkboard", 40)
        self.myFont2 = pygame.font.SysFont("chalkboard", 24)
        self.score = 0
        self.levscore = 0
        self.margin = 40
        self.click = None
        self.firstclick = None
        self.startLev = False
        self.faceLeft = False
        self.counter = True
        self.levStart = False
        self.dead = False
        self.Lost = False
        self.xSize = 15
        self.ySize = 25
        self.big = False
        self.highX = None
        self.highY = None
        self.eraseX = 450
        self.eraseY = 60
        self.playback = False
        self.white = (255,255,255)
        self.stillShip = pygame.transform.scale(
            pygame.image.load('MarioStill.png').convert_alpha(),
            (self.xSize, self.ySize))
        self.finalLength = 3000
   
    def music(self):
        
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        pygame.mixer_music.load("Mario.mp3")
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1,5)

    def Gameinit(self):
        Cloud.init()   
        self.Cloud = pygame.sprite.Group()
        for i in range (20):
            x = random.randint(0, self.finalLength)
            self.Cloud.add(Cloud(x, 80))  
                        
        Ground.init()
        self.Ground = pygame.sprite.Group()
        for i in range (20):
            x = 20+40*i
            self.Ground.add(Ground(x,self.height))

        self.shipGroup = pygame.sprite.Group(Ship(0,self.base,self.stillShip))
        
        MysteryBlock.init()
        self.mblocks = pygame.sprite.Group()
        for i in range (3):
            x = 200+40*i 
            self.mblocks.add(MysteryBlock(x,self.base-40))
        self.mblocks.add(MysteryBlock(1080,250))
        
   
    
        Tube.init()
        self.tubes = pygame.sprite.Group(Tube(750,self.base))
    
        Koopa.init()
        self.Koopas = pygame.sprite.Group(Koopa(200,200,100))
        self.Koopas.add(Koopa(700,self.base,100))
        
        self.Koopas.add(Koopa(100,self.base-60,100))

        
        self.Koopas.add(Koopa(950,self.base, 50))
        self.Koopas.add(Koopa(900,260, 80))
        self.Koopas.add(Koopa(1150,250,25))
        
        self.Koopas.add(Koopa(1225,190,25))
        self.Koopas.add(Koopa(1350,230,100))
        self.Koopas.add(Koopa(1400,self.base,100))
        self.Koopas.add(Koopa(1400,140, 25))
        self.Koopas.add(Koopa(1800,self.base,100))
        self.Koopas.add(Koopa(1700,self.base, 50))
        

    
        Block.init()
        self.blocks = pygame.sprite.Group()
        for i in range (5,0,-1):
            for j in range (i):
                x = 400+40*i
                y = self.base - 10 - 40*j
                self.blocks.add(Block(x,y))
            
        for i in range (3): 
            x = 600+40*i
            self.blocks.add(Block(x,300))
        
        for i in range (4):
            x = 760+40*i
            self.blocks.add(Block(x,300))
        
        self.blocks.add(Block(1000,250))
        self.blocks.add(Block(1040,250))


        for i in range (5,0,-1):
            for j in range (i):
                x = 1000+40*i
                y = self.base - 10 - 40*j
                self.blocks.add(Block(x,y))
        
        for i in range (5,0,-1):
            for j in range (i):
                x = 1300+40*j
                y = self.base - 10 - 40*i
                self.blocks.add(Block(x,y))
                
        for i in range (2):
            self.blocks.add(Block(1200+40*i,self.base))
            self.blocks.add(Block(1200+40*i,self.base-self.margin))
            self.blocks.add(Block(1200+40*i,self.base-self.margin*2))
            self.blocks.add(Block(1200+40*i,self.base-self.margin*3))
            self.blocks.add(Block(1200+40*i,self.base-self.margin*4))
            self.blocks.add(Block(1200+40*i,self.base-self.margin*5))
            self.blocks.add(Block(1200+40*i,self.base-self.margin*6))

        
        for i in range (5,0,-1):
            for j in range (i):
                x = 1500+40*j
                y = self.base- 200 + 40*i
                self.blocks.add(Block(x,y))
        
        self.blocks.add(Block(1340, 160))
        self.mblocks.add(MysteryBlock(1380, 160))
        self.blocks.add(Block(1420, 160))
        
        self.blocks.add(Block(1550, 240))
        self.mblocks.add(MysteryBlock(1590,240))
        self.blocks.add(Block(1630, 240))
        
        
        self.blocks.add(Block(1810, self.base-60))
        self.mblocks.add(MysteryBlock(1850,self.base-60))
        self.blocks.add(Block(1890,self.base- 60))
        
        self.blocks.add(Block(2240,self.base-210))
        self.blocks.add(Block(2280,self.base-210))
        self.blocks.add(Block(2320,self.base-210))
        self.blocks.add(Block(2360,self.base-210))
        
        self.mblocks.add(MysteryBlock(2440, self.base-105))
        
        self.blocks.add(Block(2480,self.base-210))
        self.blocks.add(Block(2520,self.base-210))
        self.blocks.add(Block(2560,self.base-210))
        self.blocks.add(Block(2600,self.base-210))


        
        self.mblocks.add(MysteryBlock(2300, self.base-100))
        
        self.Koopas.add(Koopa(2300,self.base,100))
        self.Koopas.add(Koopa(2350,self.base,100))
        self.Koopas.add(Koopa(2500,self.base-4*self.margin,100))
        
        
        for i in range (5,0,-1):
            for j in range (i):
                x = 2700+40*j
                y = self.base- 200 + 40*i
                self.blocks.add(Block(x,y))
        
        for i in range (5,0,-1):
            for j in range (i):
                x = 2000+40*i
                y = self.base - 10 - 40*j
                self.blocks.add(Block(x,y))

                


        Coin.init()
        self.coins = pygame.sprite.Group()
        
        Shroom.init()
        self.shrooms = pygame.sprite.Group()
        
    
        Pole.init()
        self.pole = pygame.sprite.Group()
        self.pole.add(Pole(3000,self.base-140))
    
    def levGroups(self):
        self.levCloud = pygame.sprite.Group()
        self.levGround = pygame.sprite.Group()
        self.levtubes = pygame.sprite.Group()
        self.levblocks = pygame.sprite.Group()
        self.levkoopas = pygame.sprite.Group()
        self.levmblocks = pygame.sprite.Group()
        self.levpole = pygame.sprite.Group()
        self.levcoins = pygame.sprite.Group()
        self.levshrooms = pygame.sprite.Group()
        self.Mario = pygame.sprite.Group()
        
    def clickGroups(self):
        self.clickCloud = \
        pygame.sprite.Group(Cloud(self.margin,self.margin*2))
       
        self.clickBlock = \
        pygame.sprite.Group(Block(self.margin,self.margin*3.5)) 
        
        self.clickMblock = \
        pygame.sprite.Group(MysteryBlock(self.margin,self.margin*5)) 
        
        self.clickGround = \
        pygame.sprite.Group(Ground(self.margin,self.margin*6.5)) 
        
        self.clickGround = \
        pygame.sprite.Group(Ground(self.margin,self.margin*6.5)) 
        
        self.clickKoopa = \
        pygame.sprite.Group(Koopa(self.margin,self.margin*8,0)) 
        
        self.clickPole = \
        pygame.sprite.Group(Pole(self.margin,self.margin*9.5))
        for pole in self.clickPole:
            pole.scale(40,40)
        
        self.clickMario = pygame.sprite.Group(Ship(self.margin,self.margin*11,self.stillShip))
    
        
        Eraser.init()
        self.clickEraser = pygame.sprite.Group(Eraser(self.width-self.margin,self.margin*2))
        
            
    def levelInit(self):
        TitleScreen.init()
        self.TitleScreen = pygame.sprite.Group(TitleScreen(self.width//2,
                                                        self.height//2+50))
        Background.init()   
        self.Background = pygame.sprite.Group(Background(self.width//2,                                                        
                                              self.height//2))
        
        self.playback = False
      
        Game.levGroups(self)
        Game.clickGroups(self)
        
        
    
    def init(self):
        Game.baseVals(self)
        TitleScreen.init()
        self.TitleScreen = pygame.sprite.Group(TitleScreen(self.width//2,
                                                        self.height//2+50))
        Background.init()   
        self.Background = pygame.sprite.Group(Background(self.width//2,                                                        
                                              self.height//2)) 
        GameOver.init()
        self.GG = pygame.sprite.Group(GameOver(self.width//2,                                                        
                                              self.height//2))
 
        WinScreen.init()
        self.Wscreen = pygame.sprite.Group(WinScreen(self.width//2,                                                        
                                              self.height//2))
 
        Game.Gameinit(self)
        Game.levelInit(self)
    
    
    
    def images(self):
        self.stillShip = pygame.transform.scale(
            pygame.image.load('MarioStill.png').convert_alpha(),
            (self.xSize, self.ySize))
        self.leftstillship =  pygame.transform.flip(self.stillShip, True, False)
        self.rightShip = pygame.transform.scale(
            pygame.image.load('MarioRight.png').convert_alpha(),
            (self.xSize, self.ySize))
        self.leftShip = pygame.transform.flip(self.rightShip, True, False)
        
        self.rightShip2 = pygame.transform.scale(
            pygame.image.load('Mariomotion.png').convert_alpha(),
            (self.xSize, self.ySize))
       
        self.leftShip2 = pygame.transform.flip(self.rightShip2, True, False)
        
        
        #All images above credited to
        #http://sketchnation.com/SketchNationTutorialComputerGraphics.html
        
        self.jumpShip = pygame.transform.scale(pygame.image.load('MarioLeft.png').convert_alpha(), (self.xSize, self.ySize))
      #Credited To   http://www.thevideogamegallery.com/gallery/image:21558/super-mario-bros:sprite-mario-jumping
        
        self.jumpShip2 =  pygame.transform.flip(self.jumpShip, True, False)
        
        
        
        
    def runUpdates(self):
        Game.images(self)
        
        if (self.running == True):
            self.shipGroup.update(self.isKeyPressed, self.width, self.height)
            self.Koopas.update(self.width,self.height)
            self.blocks.update(self.width,self.height)
            self.Cloud.update(self.width,self.height)
            self.tubes.update(self.width,self.height)
            self.coins.update(self.width,self.height)
            self.mblocks.update(self.width,self.height)
            self.pole.update(self.width,self.height)
            self.shrooms.update(self.width,self.height)
            
        elif (self.levelDesign == True or self.levStart == True):
            self.levGround.update(self.width,self.height)
            self.levblocks.update(self.width,self.height)
            self.Mario.update(self.isKeyPressed,self.width,self.height)
            self.levpole.update(self.width,self.height)
            self.levCloud.update(self.width,self.height)
            self.levkoopas.update(self.width,self.height)
            self.levmblocks.update(self.width,self.height)
            self.levcoins.update(self.width,self.height)
            self.levshrooms.update(self.width,self.height)
    
    def checkMario(self,shipGroup):
        for ship in shipGroup:
            if ship.getY() > self.height:
                self.Lost = True

    def PoleCollide(self):
        if (self.running == True):
            if pygame.sprite.groupcollide(
                self.pole, self.shipGroup, False, False,
                pygame.sprite.collide_rect):
                self.running = False
                self.end = True
        if (self.levStart == True):
            if pygame.sprite.groupcollide(
                self.levpole, self.Mario, False, False,
                pygame.sprite.collide_rect):
                self.levStart= False
                self.end = True

                
    def match(mx,my,x,y):
        if (mx > x-40 and mx < x + 40):
            if (my > y-40 and my < y + 40):
                return True
        return False


    def levDesign(self):
        mX = self.mousePos()[0]
        mY = self.mousePos()[1]
        Game.runUpdates(self)
        pressed = self.mousePressed(mX,mY)
        for ground in self.clickGround:
            x = ground.getX() 
            y = ground.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Ground"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for block in self.clickBlock:
            x = block.getX() 
            y = block.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Block"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for mario in self.clickMario:
            x = mario.getX()
            y = mario.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Mario"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for pole in self.clickPole:
            x = pole.getX()
            y = pole.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Pole"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for koopa in self.clickKoopa:
            x = koopa.getX()
            y = koopa.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Koopa"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for mblock in self.clickMblock:
            x = mblock.getX()
            y = mblock.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Mblock"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for cloud in self.clickCloud:
            x = cloud.getX()
            y = cloud.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Cloud"
                self.firstclick = True
                self.highX = x
                self.highY = y
        for eraser in self.clickEraser:
            x = eraser.getX()
            y = eraser.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.click = "Eraser"
                self.firstclick = True
                self.highX = x
                self.highY = y
                
        Game.addElements(self)
        Game.levScroll(self)
    
    
    def deleteElements(self):
        mX = self.mousePos()[0]
        mY = self.mousePos()[1]
        Game.runUpdates(self)
        pressed = self.mousePressed(mX,mY)
        for ground in self.levGround:
            x = ground.getX() 
            y = ground.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.levGround.remove(ground)
        for block in self.levblocks:
            x = block.getX() 
            y = block.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.levblocks.remove(block)
        for mario in self.Mario:
            x = mario.getX()
            y = mario.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.Mario.remove(mario)
        for pole in self.levpole:
            x = pole.getX()
            y = pole.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.levpole.remove(pole)
        for koopa in self.levkoopas:
            x = koopa.getX()
            y = koopa.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.levkoopas.remove(koopa)
        for mblock in self.levmblocks:
            x = mblock.getX()
            y = mblock.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.levmblocks.remove(mblock)
        for cloud in self.levCloud:
            x = cloud.getX()
            y = cloud.getY()
            if (pressed ==1 and Game.match(mX,mY,x,y) == True):
                self.levCloud.remove(cloud)
        
    
    def addElements(self):
        mX = self.mousePos()[0]
        mY = self.mousePos()[1]
        pressed = self.mousePressed(mX,mY)
        if self.click == "Ground":
            if (pressed == 1) and self.firstclick == True:
                self.firstclick = False
            elif (pressed == 1 and self.firstclick == False):
                self.levGround.add(Ground(mX,mY))
        elif self.click == "Block":
            if (pressed == 1 and self.firstclick == True):
                self.firstclick = False
            elif (pressed == 1 and self.firstclick == False):
                self.levblocks.add(Block(mX,mY))
        elif self.click == "Pole":
            if (len(self.levpole) < 1):
                if (pressed == 1 and self.firstclick == True):
                    self.firstclick = False
                elif (pressed == 1 and self.firstclick == False):
                    self.levpole.add(Pole(mX,mY))
        elif self.click == "Mblock":           
            if (pressed == 1 and self.firstclick == True):
                self.firstclick = False
            elif (pressed == 1 and self.firstclick == False):
                self.levmblocks.add(MysteryBlock(mX,mY))
        elif self.click == "Koopa":
            if (pressed == 1 and self.firstclick == True):
                self.firstclick = False
            elif (pressed == 1 and self.firstclick == False):
                self.levkoopas.add(Koopa(mX,mY,100))
        elif self.click == "Cloud":
            if (pressed == 1 and self.firstclick == True):
                self.firstclick = False
            elif (pressed == 1 and self.firstclick == False):
                self.levCloud.add(Cloud(mX,mY))
        elif self.click == "Mario":
            if (len(self.Mario) < 1):
                if (pressed == 1 and self.firstclick == True):
                    self.firstclick = False
                elif (pressed == 1 and self.firstclick == False):
                    self.Mario.add(Ship(mX,mY,self.stillShip))
        elif self.click == "Eraser":
            Game.deleteElements(self)
 
    
    def initMode(self):
        if (self.isKeyPressed(pygame.K_p)):
            Game.init(self)
            if (self.big == True):
                self.xSize = 15
                self.ySize = 25
            self.start = False
            self.running = True
            self.levelDesign = False
            Game.music(self)
            self.levStart = False
            self.big = False

        if (self.levelDesign == True):
            Game.levDesign(self)
           
        if (self.isKeyPressed(pygame.K_k)):
            Game.Gameinit(self)
        
        if (self.isKeyPressed(pygame.K_l)):
            self.start = False
            self.running = False
            Game.levelInit(self)
            self.levelDesign = True
            self.levStart = False
            self.Lost = False
            if (self.big == True):
                self.xSize = 15
                self.ySize = 25
        
        if (self.isKeyPressed(pygame.K_w) and len(self.Mario) == 1):
            self.running = False
            self.levelDesign = False
            self.levStart = True
            
    def blockCollide(self,shipGroup, blocks):
        for ship in shipGroup:
            for block in blocks: 
                if pygame.sprite.collide_rect(ship,block):
                    if (ship.getY()+20 >= block.getY()):
                        ship.fall()
                    elif (ship.getY()-20 <= block.getY()):
                        ship.setAir(False)

        for mario in shipGroup:
            for block in blocks:
                if pygame.sprite.collide_rect(mario,block):
                    if (mario.getY() - 20 <= block.getY() 
                        and mario.getY()+ 20 >= block.getY()):
                        if (mario.getX() + 30 >= block.getX()):
                            mario.stopMoving(self.isKeyPressed, self.faceLeft)
                            
    
    def shroomBlock(self, shrooms, blocks):
        for shroom in shrooms:
            for block in blocks:
                if pygame.sprite.collide_rect(shroom,block):
                    if (shroom.getY()-20 <= block.getY()):
                        shroom.setAir(False)
    
                     
                else:
                    shroom.setAir(True)
                
    
    def shroomMBlock(self, shrooms, mblocks):
        for shroom in shrooms:
            for block in mblocks:
                if pygame.sprite.collide_rect(shroom,block):
                    if (shroom.getY()-20 <= block.getY()):
                        shroom.setAir(False)
                
    
    
  
    def mblockCoinHandle(self,mblocks,coins,blocks):
        for coin in coins:
            initY = coin.getinitY()
            coin.coinMove()
            if (initY-coin.getY() > 6):
                coins.remove(coin)
                coin.coinSound()
                if (self.running == True):
                    self.score += 25
                elif (self.levStart == True):
                    self.levscore += 25
                for mblock in mblocks:
                    if mblock.getX() == coin.getX():
                        mblocks.remove(mblock)
                        blocks.add(Block(mblock.getX(), 
                        mblock.getY()))
        
    def mblockShroomHandle(self,mblocks, shrooms):
        for shroom in shrooms:
            shroom.shroomMove()
            

    
    def groundCollide(self, ground, shipGroup):
        if pygame.sprite.groupcollide(
            ground, shipGroup, False, False,
            pygame.sprite.collide_rect):
            for ship in shipGroup:
                ship.setAir(False)
    
    
    def noCollide(self, blocks, ground, shipGroup):
        if not pygame.sprite.groupcollide(
            ground, shipGroup, False, False,
            pygame.sprite.collide_rect) and not pygame.sprite.groupcollide(
            blocks, shipGroup, False, False,
            pygame.sprite.collide_rect):
            for ship in shipGroup:
                ship.setAir(True)

                            

    
    def koopaCollide(self, koopas, shipGroup):
        for ship in shipGroup:
            for koopa in koopas:
                if pygame.sprite.collide_rect(ship,koopa):
                    if (ship.getY() - 10 <= koopa.getY() 
                        and ship.getY()+ 10 >= koopa.getY()):
                        if (ship.getX() + 20 >= koopa.getX()):
                            if (self.big == False):
                                self.dead = True
                                ship.deadAction()
                                ship.die()
                                ship.Move(0,0)
                                self.dead = False
                            elif (self.big == True):
                                self.xSize = 15
                                self.ySize = 25
                                pygame.mixer.Sound("PowerDown.OGG").play()
                    elif (ship.getY() <= koopa.getY() and ship.getY() + self.margin >= koopa.getY()):
                        if (ship.getX() - 30 <= koopa.getX() 
                            and ship.getX()+ 30 >= koopa.getX()):
                            ship.setAir(False)
                            koopa.deathSound()
                            koopas.remove(koopa)
                            ship.moveUp()
                            if (self.running == True):
                                self.score += 100
                            elif (self.levStart == True):
                                self.levscore +=100
                          
    def koopaBlockXcollide(self, blocks, koopas):
        for koopa in koopas:
            for block in blocks:
                if pygame.sprite.collide_rect(koopa,block):
                    if (koopa.getY() - 20 <= block.getY() 
                        and koopa.getY()+ 20 >= block.getY()):
                        if (koopa.getX() + 30 >= block.getX()):
                            koopa.changeCounter()
            

    def ensurePowerDown(self, koopas, shipGroup):
        if not pygame.sprite.groupcollide(
            koopas,shipGroup, False, False, pygame.sprite.collide_rect): 
            if self.xSize == 15 and self.ySize == 25: 
                self.big = False

    def shroomCollide(self, shipGroup, shrooms):
        if pygame.sprite.groupcollide(
            shrooms,shipGroup, True, False,
            pygame.sprite.collide_rect):
            pygame.mixer.Sound("Shroom.OGG").play()
            if (self.big == False):
                self.xSize = int(self.xSize * 1.25)
                self.ySize = int(self.ySize * 1.25)
                self.big = True
            if (self.running == True):
                self.score +=100
            elif (self.levStart == True):
                self.levscore += 100
                
    def checkforDead(self, shipGroup):
        for ship in shipGroup:
            if ship.getLives() == 0:
                self.Lost = True
                self.running = False
                self.levStart = False
                self.levDesign = False
    
    
    def mBlockCollide(self,shipGroup,mblocks,koopas):
        for ship in shipGroup:
            for mblock in mblocks:
                if pygame.sprite.collide_rect(ship,mblock):
                    if (ship.getX() <= mblock.getX()+self.margin//2 and 
                        ship.getX() >= mblock.getX()-self.margin//2):
                        if (ship.getY()+10 <= mblock.getY()):
                            ship.setAir(False)
                        elif (ship.getY()+10>= mblock.getY()):
                            num = random.randint(1,10)
                            for koopa in koopas:
                                if pygame.sprite.collide_rect(mblock,koopa):
                                    koopa.deathSound()
                                    koopas.remove(koopa)
                                    if (self.running == True):
                                        self.score+=100
                                    elif (self.levStart == True):
                                        self.levscore += 100
                            ship.fall()
                            if num > 3:
                                x = mblock.getX()
                                y = mblock.getY()-self.margin
                                if (self.running == True):
                                    self.coins.add(Coin(x,y))
                                elif (self.levStart == True):
                                    self.levcoins.add(Coin(x,y))
                            elif num < 3: 
                                x = mblock.getX()
                                y = mblock.getY()
                                shroomy = mblock.getY()-self.margin//1.5
                                if self.running == True:
                                    self.mblocks.remove(mblock)
                                    self.blocks.add(Block(x,y))
                                    self.shrooms.add(Shroom(x,shroomy))
                                elif self.levStart == True:
                                    self.levmblocks.remove(mblock)
                                    self.levblocks.add(Block(x,y))
                                    self.levshrooms.add(Shroom(x,shroomy))
        for mario in shipGroup:
            for block in mblocks:
                if pygame.sprite.collide_rect(mario,block):
                    if (mario.getY() - 20 <= block.getY() 
                        and mario.getY()+ 20 >= block.getY()):
                        if (mario.getX() + 30 >= block.getX()):
                            mario.stopMoving(self.isKeyPressed, self.faceLeft)
            
    def startMoving(self,shipGroup,blocks,mblocks,tubes):
        if not pygame.sprite.groupcollide(
            mblocks, shipGroup, False, False,
            pygame.sprite.collide_rect) and not pygame.sprite.groupcollide(
            blocks, shipGroup, False, False,
            pygame.sprite.collide_rect) and not pygame.sprite.groupcollide(
            tubes, shipGroup, False, False,
            pygame.sprite.collide_rect):
            for ship in self.shipGroup:
                ship.startMoving(self.isKeyPressed)
            
                    
    def timerFired(self, dt):
        Game.initMode(self)
       
                
                
        if (self.levStart == True):
            Game.runUpdates(self)
            Game.blockCollide(self,self.Mario,self.levblocks)
            Game.animation(self,self.Mario)
            Game.noCollide(self,self.levblocks,self.levGround,self.Mario)
            Game.mblockCoinHandle(self, self.levmblocks, self.levcoins,self.levblocks)
            Game.koopaCollide(self, self.levkoopas, self.Mario)
            Game.blockCollide(self,self.Mario,self.levtubes)
            Game.mblockShroomHandle(self, self.levmblocks, self.levshrooms)
            Game.PoleCollide(self)
            Game.checkMario(self,self.Mario)
            Game.checkforDead(self,self.Mario)
            Game.shroomCollide(self, self.Mario, self.levshrooms)
            Game.blockCollide(self, self.Mario, self.levGround)
       
            Game.ensurePowerDown(self, self.levkoopas, self.Mario)
       
            Game.shroomBlock(self,self.levshrooms,self.levblocks)
            Game.shroomMBlock(self,self.levshrooms,self.levmblocks)
            Game.groundCollide(self, self.levGround, self.levshrooms)
            
            Game.koopaBlockXcollide(self,self.levblocks,self.levkoopas)
            
            Game.mBlockCollide(self,self.Mario,self.levmblocks,self.levkoopas)
            Game.Scroll(self)
            if not pygame.sprite.groupcollide(
                self.levmblocks, self.Mario, False, False,
                pygame.sprite.collide_rect) and not    pygame.sprite.groupcollide(
                self.levblocks, self.Mario, False, False,
                pygame.sprite.collide_rect):
                for ship in self.Mario:
                    ship.startMoving(self.isKeyPressed)
        
        

        
        if (self.running == True):
            Game.runUpdates(self)
            Game.PoleCollide(self)
            Game.checkMario(self,self.shipGroup)
            Game.checkforDead(self,self.shipGroup)

            Game.blockCollide(self,self.shipGroup,self.Ground)
            Game.mblockCoinHandle(self, self.mblocks, self.coins,self.blocks)
            Game.mblockShroomHandle(self, self.mblocks, self.shrooms)
            Game.blockCollide(self,self.shipGroup,self.blocks)
            Game.noCollide(self,self.blocks,self.Ground, self.shipGroup)
            Game.blockCollide(self, self.shipGroup,self.tubes)
            Game.koopaCollide(self, self.Koopas, self.shipGroup)
            Game.shroomCollide(self, self.shipGroup, self.shrooms)
            
       
            Game.shroomBlock(self,self.shrooms,self.blocks)
            Game.shroomMBlock(self,self.shrooms,self.mblocks)
            Game.groundCollide(self, self.Ground, self.shrooms)
            
            Game.koopaBlockXcollide(self,self.blocks,self.Koopas)
            Game.koopaBlockXcollide(self,self.tubes,self.Koopas)
            Game.koopaBlockXcollide(self, self.mblocks, self.Koopas)
    
            Game.ensurePowerDown(self, self.Koopas,self.shipGroup)
    
            Game.mBlockCollide(self,self.shipGroup,self.mblocks,self.Koopas)

            Game.startMoving(self,self.shipGroup,self.blocks,self.mblocks,self.tubes)
            
            
            
            Game.animation(self,self.shipGroup)
            Game.Scroll(self)
    
    
    
    
    def animation(self,shipGroup):
            
            if (self.isKeyPressed(pygame.K_RIGHT)):
                for ship in shipGroup:
                    if ship.getAir() == True:
                        ship.changeImage(self.jumpShip)
                    else:
                        time = pygame.time.get_ticks()
             
                        if (time // 100 % 2 ==0):
                            ship.changeImage(self.rightShip)
                            self.counter = False
    
                        elif (time // 100 % 2 !=0):
                            ship.changeImage(self.rightShip2)
                            self.counter = True 
                    
                    
                self.faceLeft = False
            
            
            elif (self.isKeyPressed(pygame.K_LEFT)):
                for ship in shipGroup:
                    if ship.getAir() == True:
                        ship.changeImage(self.jumpShip2)
                        
                    else:
                        time = pygame.time.get_ticks()
              
                        if (time // 100 % 2 ==0):
                            ship.changeImage(self.leftShip)
                            self.counter = False
    
                        elif (time // 100 % 2 !=0):
                            ship.changeImage(self.leftShip2)
                            self.counter = True 
                    
                self.faceLeft = True
        
            
            else:
                if (self.faceLeft == False):
                    for ship in shipGroup:
                        if (ship.getAir() == False):
                            ship.changeImage(self.stillShip)
                        else:
                            ship.changeImage(self.jumpShip)

                elif (self.faceLeft == True):
                    for ship in shipGroup:
                        if (ship.getAir() == False):
                            ship.changeImage(self.leftstillship)
                        else:
                            ship.changeImage(self.jumpShip2)
    
        
      
    def Scroll(self):
        if (self.running == True):
            for mario in self.shipGroup:
                Xcoord = mario.getX()
                if (Xcoord >= self.width//2 ):
                    mario.setX(3)
                    for block in self.blocks:
                        block.setX(1.5)
                    for koopa in self.Koopas:
                        koopa.setX(1.5)
                    for cloud in self.Cloud:
                        cloud.setX(1.5)
                    for tube in self.tubes:
                        tube.setX(1.5)
                    for coin in self.coins:
                        coin.setX(1.5)
                    for mblock in self.mblocks:
                        mblock.setX(1.5)
                    for pole in self.pole:
                        pole.setX(1.5)
                    for shroom in self.shrooms:
                        shroom.setX(1.5)
        if (self.levStart == True):
            for mario in self.Mario:
                Xcoord = mario.getX()
                if (Xcoord >= self.width//2 ):
                    mario.setX(3)
                    for block in self.levblocks:
                        block.setX(1.5)
                    for koopa in self.levkoopas:
                        koopa.setX(1.5)
                    for cloud in self.levCloud:
                        cloud.setX(1.5)
                    for tube in self.levtubes:
                        tube.setX(1.5)
                    for coin in self.levcoins:
                        coin.setX(1.5)
                    for mblock in self.levmblocks:
                        mblock.setX(1.5)
                    for pole in self.levpole:
                        pole.setX(1.5)
                    for shroom in self.levshrooms:
                        shroom.setX(1.5)
                    for ground in self.levGround:
                        ground.setX(1.5)
                        
    def valofScroll(self, val):
            for block in self.levblocks:
                block.setX(val)
            for koopa in self.levkoopas:
                koopa.setX(val)
            for cloud in self.levCloud:
                cloud.setX(val)
            for tube in self.levtubes:
                tube.setX(val)
            for mblock in self.levmblocks:
                mblock.setX(val)
            for pole in self.levpole:
                pole.setX(val)
            for ground in self.levGround:
                ground.setX(val)
            for mario in self.Mario:
                mario.setX(val)
            for shroom in self.levshrooms:
                shroom.setX(val)
                
    def levScroll(self):
        if (self.isKeyPressed(pygame.K_d)):
            Game.valofScroll(self, -5)
        elif (self.isKeyPressed(pygame.K_a)):
            Game.valofScroll(self, 5)

    def Text(self, screen):
        label = self.myFont.render("Mario", 30, self.white)
        screen.blit(label, (0, -10))
        world = self.myFont.render("World", 30, self.white)
        screen.blit(world, (300, -10))
        point = self.myFont.render("1-1", 30, self.white)
        screen.blit(point, (365, 20))
        LifeFont = self.myFont.render("Lives", 1, self.white)
        screen.blit(LifeFont, (self.width-self.width//8, -10))


    def endGameText(self,screen):
            
        main = self.myFont.render("Main Level", 1, self.white)
        nextmain = self.myFont.render("Score:", 1, self.white)
        label = self.myFont.render(str(self.score), 1, self.white)
        
        designed = self.myFont.render("Designed Level", 1, self.white)
        nextDes = self.myFont.render("Score:", 1, self.white)
        levlabel = self.myFont.render(str(self.levscore), 1, self.white)
        
        again = self.myFont.render("Press P to Play" ,1, self.white)
        againCont = self.myFont.render("default Level!!!" ,1, self.white)
        
        levagain = self.myFont.render("Press L to Create" ,1, self.white)
        levagainCont = self.myFont.render("a new Level!!!" ,1, self.white)
        
        
        if (self.Lost == True):
            screen.blit(again,(self.width-self.width//2.8,self.margin*2))
            screen.blit(againCont,(self.width-self.width//2.8,self.margin*3-self.margin//4))
            
            screen.blit(levagain, (self.width-self.width//2.5, self.margin*6))
            screen.blit(levagainCont, (self.width-self.width//2.5, self.margin*7-self.margin//4))
        
        elif (self.end == True):
            screen.blit(again,(0,self.margin*6))
            screen.blit(againCont,(0,self.margin*7-self.margin//4))
            
            screen.blit(levagain, (0, self.margin*8.5))
            screen.blit(levagainCont, (0, self.margin*9.5-self.margin//4))
        
        
        screen.blit(label, (0, self.margin+self.margin//2))
        screen.blit(nextmain,(0,self.margin//2+self.margin//4))
        screen.blit(main, (0,0))
        
        screen.blit(levlabel, (0, self.margin*4+self.margin//2))
        screen.blit(nextDes,(0,self.margin*3+3*self.margin//4))
        screen.blit(designed, (0,self.margin*3))

    def drawLevgameObjects(self, screen):
            self.levGround.draw(screen)
            self.levblocks.draw(screen)
            self.Mario.draw(screen)
            self.levpole.draw(screen)
            self.levmblocks.draw(screen)
            self.levkoopas.draw(screen)
            self.levCloud.draw(screen)
            self.levcoins.draw(screen)

    def redrawAll(self, screen):
        if (self.start == True):
            self.TitleScreen.draw(screen)
            option = self.myFont2.render("Press L to Create!!!" ,1, (0,0,0))
            screen.blit(option, (self.width-self.width//2, 0.9*self.base))
            Name = self.myFont2.render("By Shivum Agarwal" ,1, (0,0,0))
            screen.blit(Name, (self.width//4, 0.95*self.base))


        elif (self.Lost == True):
            pygame.mixer_music.stop()
            self.GG.draw(screen)
            if (self.playback == False):
                self.playback = True
                pygame.mixer.Sound("GameOver.OGG").play(0)
            Game.endGameText(self,screen)
        


        elif (self.running == True):
            self.Background.draw(screen)
            Game.Text(self,screen)
            
            self.Cloud.draw(screen)
            self.shipGroup.draw(screen)
            self.blocks.draw(screen)
            self.Koopas.draw(screen)
            self.tubes.draw(screen)
            self.coins.draw(screen)
            self.mblocks.draw(screen)
            label = self.myFont.render(str(self.score), 1, self.white)
            screen.blit(label, (0, self.margin//2))
            self.Ground.draw(screen)
            self.pole.draw(screen)
            self.shrooms.draw(screen)
            
            
          
            
            for mario in self.shipGroup:
                num = mario.getLives()
            lives = self.myFont.render(str(num), 1, self.white)
            screen.blit(lives, (self.width-self.width//24, self.margin//2))
            
        elif (self.levelDesign == True):
            self.Background.draw(screen)
            label = self.myFont.render("Welcome to Level Design", 1, (0,0,0))
            screen.blit(label, (self.width//8, 0))
            
            Text = self.myFont.render("Eraser", 1, (0,0,0))
            screen.blit(Text, (self.width-self.width//6, 0))
            
            instruct = self.myFont2.render("Use A and D keys to scroll left and right respectively!", 1, self.white)
            screen.blit(instruct, (self.width//8, self.margin))
            
            instructCont = self.myFont2.render("Press W to start Level!!", 1, self.white)
            screen.blit(instructCont, (self.width//8, 3*self.margin/2))

            if (self.highX != None and self.highY != None):
                x1 = self.highX-25
                y1 = self.highY-25
                pygame.draw.rect(screen,(0,255,0),(x1,y1,50,50),0)
            self.clickCloud.draw(screen)
            self.clickBlock.draw(screen)
            self.clickGround.draw(screen)
            self.clickKoopa.draw(screen)
            self.clickMblock.draw(screen)
            self.clickPole.draw(screen)
            self.clickMario.draw(screen)
            
            Game.drawLevgameObjects(self, screen)
            self.clickEraser.draw(screen)

        elif(self.levStart == True):
            self.Background.draw(screen)
            Game.Text(self,screen)
            for mario in self.Mario:
                num = mario.getLives()
            label = self.myFont.render(str(num), 1, self.white)
            screen.blit(label, (self.width-self.width//24, self.margin//2))
            Game.drawLevgameObjects(self, screen)
            nlabel = self.myFont.render(str(self.levscore), 1, self.white)
            screen.blit(nlabel, (0, self.margin//2))
            

            
            
        elif (self.end == True):
            pygame.mixer_music.stop()
            self.Wscreen.draw(screen)
            Game.endGameText(self,screen)
            label = self.myFont.render("CONGRATS YOU WIN!!!!!!", 1, self.white)
            screen.blit(label, (self.width//3, 0))
            if (self.playback == False):
                self.playback = True
                pygame.mixer.Sound("Win.OGG").play(0)
    

Game(800, 500).run()