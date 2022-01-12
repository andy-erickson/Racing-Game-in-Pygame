
import pygame
from random import randint
   
        
class CarStats:
    def __init__(self, speed, lr, clock, fuel=60):
        self.speed = speed
        self.lr = lr
        self.throttle = False
        self.brake = False
        self.clock = clock
        self.fuel = fuel

    def finalDrive(self):
        if self.throttle == True:
            if self.clock < 100:
                self.speed += 2
            if 100 <= self.clock < 150:
                self.speed += 1
            if 150 <= self.clock < 199:
                self.speed += .5
            self.fuel -= .01
        else:
            if self.speed > 0 and self.clock > 0:
                self.speed -= .75

        try:
            car.clock = 1 + int (10 *(car.speed**.4))
        except:
            print('broke')
            car.clock = 1
            car.speed = 10            
    
        if car.speed < 10:
            car.clock = 1
            car.speed = 10          

    def brakes(self):
        self.speed -= 4
        
        
class Crash:
    def __init__(self,damage=0):
        self.damage = damage
        self.gameover = False
        
    def offTrackDecel(self):
        if self.speed > 100:
            self.speed -= 3
        else:
            self.speed -= 1.8
        

    def offTrackShake(self,mult=1):
        if self.speed < 100:
            self.lr += randint(-1*mult, 1*mult)
        else:
            self.lr += randint(-2*mult, 2*mult)
        
        if 30 < self.lr < 100:
            self.lr -= 1
        elif 400 < self.lr < 470:
            self.lr += 1
        

    def hitBush(self):
        self.speed -= 3
        

    def gameOver(self):
        self.gameover = True
        
        
class Images:
    def __init__(self):
        self.background1 = pygame.image.load("straight1r2.png").convert()
        self.background2 = pygame.image.load("straight2r2.png").convert()
        self.cluster = pygame.image.load("cluster2.png").convert_alpha()
        self.fuelGauge = pygame.image.load("fuelGauge.png").convert_alpha()
        self.damageGauge = pygame.image.load("damageGauge.png").convert_alpha()
        self.greenCarStraight = pygame.image.load("greenCarFinal1.png").convert_alpha()
        #self.layover = pygame.image.load("3DLayover.png").convert_alpha()
        self.statFont = pygame.font.SysFont("times", 30)
        self.buttonFont = pygame.font.SysFont("times", 12)
        self.clusterFont = pygame.font.SysFont("impact", 30)
        
    def draw(self,i,j=0):
        
        self.bush1 = pygame.draw.rect(win, (0,0,0), (540, i+100, 50 , 50))
        self.bush2 = pygame.draw.rect(win, (0,0,0), (30, i-110, 50 , 50))
        self.bush3 = pygame.draw.rect(win, (0,0,0), (590, i-360, 50 , 50))            
        win.blit(image.background1, [0, i+j])
        win.blit(image.background2, [0, i+j-400])
        win.blit(image.background1, [0, i+j-800])        
        self.carImage = win.blit(image.greenCarStraight, [car.lr, 200])
        pygame.display.flip()
        
    def drawInstructions(self):
        pygame.draw.rect(win, (0,0,0), (550, 250, 50 , 50),4)
        pygame.draw.rect(win, (0,0,0), (550, 310, 50 , 50),4)
        pygame.draw.rect(win, (0,0,0), (490, 310, 50 , 50),4)
        pygame.draw.rect(win, (0,0,0), (610, 310, 50 , 50),4)
        win.blit(image.buttonFont.render(f'Throttle', 1, (0,0,0)), (557, 265))
        win.blit(image.buttonFont.render(f'Brake', 1, (0,0,0)), (560, 325))
        win.blit(image.buttonFont.render(f'Left', 1, (0,0,0)), (505, 325))
        win.blit(image.buttonFont.render(f'Right', 1, (0,0,0)), (623, 325))
        pygame.display.flip()
        
    def drawGauges(self):
        #pygame.draw.rect(win, (0,200,200), (500, 10, 150 , 50))
        win.blit(image.cluster, [-4, 0])
        win.blit(image.clusterFont.render(f'{car.clock}', 1, (248,147,67)), (165, 40))
        win.blit(image.fuelGauge, [500, -7])
        win.blit(image.buttonFont.render(f'Fuel:', 1, (0,0,0)), (550, 10))
        pygame.draw.rect(win, (225,50,50), (557, 32, car.fuel, 5))
        win.blit(image.damageGauge, [510, 25])
        win.blit(image.buttonFont.render(f'Damage:', 1, (0,0,0)), (550, 45))
        pygame.draw.rect(win, (225,50,50), (557, 64, crash.damage, 5))
        

        r1000 = pygame.draw.circle(win, (248,147,67), (22,78), 7)
        r1500 = pygame.draw.circle(win, (248,147,67), (31,70), 7)
        r2000 = pygame.draw.circle(win, (248,147,67), (41,62), 7)
        r2500 = pygame.draw.circle(win, (248,147,67), (51,55), 7)
        r3000 = pygame.draw.circle(win, (248,147,67), (62,48), 7)
        r3500 = pygame.draw.circle(win, (248,147,67), (74,42), 7)
        r4000 = pygame.draw.circle(win, (248,147,67), (86,36), 7)
        r4500 = pygame.draw.circle(win, (248,147,67), (99,31), 7)
        r5000 = pygame.draw.circle(win, (248,147,67), (112,27), 7)
        r5500 = pygame.draw.circle(win, (248,147,67), (125,24), 7)
        r6000 = pygame.draw.circle(win, (248,147,67), (139,21), 7)
        r6500 = pygame.draw.circle(win, (248,137,62), (154,19), 7)
        r7000 = pygame.draw.circle(win, (248,127,57), (168,18), 7)
        r7500 = pygame.draw.circle(win, (248,117,52), (182,18), 7)
        r8000 = pygame.draw.circle(win, (248,60,30), (196,19), 7)
        pygame.display.flip()
        


pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((711,400))
pygame.display.set_caption('RaCe')
car = CarStats(speed=0, lr=250,clock=20)
image = Images()
crash = Crash()
run = True

while run:
            
    for i in range(0,800,20):
        pygame.event.pump()
        print(clock)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] == 1 :
            car.throttle = True
            CarStats.finalDrive(car)
        else:
            car.throttle = False
            CarStats.finalDrive(car)
            
        if keys[pygame.K_DOWN] == 1 :
            CarStats.brakes(car)
            
        if keys[pygame.K_RIGHT] == 1:
            car.lr += 5
            
        if keys[pygame.K_LEFT] == 1:
            car.lr -= 5
            
        if 100 > car.lr or car.lr > 400:
            Crash.offTrackDecel(car)
            Crash.offTrackShake(car)

        if car.clock < 10:
            for j in range(1,20,4):
                image.draw(i,j)
                image.drawInstructions()
                image.drawGauges()
                clock.tick(int(5/(car.clock/2)))
        else:
            image.draw(i,0)
            image.drawGauges()
            clock.tick(int(car.clock/2))
                             
            
        if image.carImage.colliderect(image.bush1) or image.carImage.colliderect(image.bush2) or image.carImage.colliderect(image.bush3):
            crash.damage += .25
            collision_tolerance = 30
            if abs(image.carImage.top - image.bush1.bottom) < collision_tolerance and car.speed > 0:
                print("HIT IT")
                Crash.hitBush(car)
                Crash.offTrackShake(car,5)
            if abs(image.carImage.top - image.bush2.bottom) < collision_tolerance and car.speed > 0:
                print("HIT IT")
                Crash.hitBush(car)
                Crash.offTrackShake(car,5)                
            if abs(image.carImage.top - image.bush3.bottom) < collision_tolerance and car.speed > 0:
                print("HIT IT")
                Crash.hitBush(car)
                Crash.offTrackShake(car,5)
                
        if crash.damage >= 60 or car.fuel < 0:
            Crash.gameOver(crash)
        while crash.gameover == True:
            pygame.event.pump()
            car.clock = 2
            car.speed = 0
            car.lr = 250
            crash.health = 0
            win.blit(image.statFont.render('GAME OVER', 1, (225,0,0)), (250, 200))
            pygame.display.flip()
            clock.tick(int(5/(car.clock/2)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
   
pygame.quit()
    