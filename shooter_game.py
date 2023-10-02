#Создай собственный Шутер!
from random import *
from pygame import *
import time as vr
#from  time import *
mixer.init()
font.init()
mixer.music.load("space.ogg")
#mixer.music.play()
ba_bah = mixer.Sound("fire.ogg")

number = 0
number_1 = 0

FIRST = 30
SEC = 5
LIFE = 4
class Spirt(sprite.Sprite):
    def __init__(self, width, height, ima, sx, sy, speed):
        sprite.Sprite.__init__(self)
        self.width = width # ширина
        self.height = height # высота
        self.ima = ima
        self.speed = speed
        self.image = transform.scale(image.load(ima),( width, height))
        self.rect = self.image.get_rect()
        self.rect.x = sx
        self.rect.y = sy
        self.life_flag = True
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(Spirt):
    def __init__(self, width, height, ima, sx, sy, speed):
        super().__init__(width, height, ima, sx, sy, speed)
        self.ammo = FIRST
        self.reloadam = False
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x < 625:
            self.rect.x+=self.speed
    def fire(self):
        if self.ammo > 0 and self.reloadam == False:
            ba_bah.play()
            self.ammo -= 1
            balets.add(Balet(5, 5, "bullet.png", self.rect.centerx,  self.rect.top, 5))
            #if self.reloadam == True:
                #global start
                #start = vr.time()
class Balet(Spirt):
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Asteroid(Spirt):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.x = randint(5, 650)
            self.rect.y = randint(-50, -10)
            self.speed = randint(2, 5)

        

class Enemy(Spirt): 
    
    def update(self):
        if self.rect.x < 650 and self.rect.x > 0:
            
            self.rect.x+=randint(-5, 5)
        elif self.rect.x >= 650:
            self.rect.x+=randint(-5, -1)
                
        elif self.rect.x <= 0:
            
            self.rect.x+=randint(1, 5)
        if self.rect.y < 700 and self.rect.y >= -51:
            
            self.rect.y+=self.speed
        else:
            global number_1
            number_1+=1
            
            self.rect.x = randint(5, 650)
            self.rect.y = randint(-50, -10)
            self.speed = randint(1, 6)
    
fon_ti = font.SysFont("Arial", 50)
fon_t = font.SysFont("Arial", 25)
fon_ni = font.SysFont("Arial", 40)

#calcul = fon_t.render("Счёт: ", True, (255, 255, 255))
fon_t_1 = font.SysFont("Arial", 25)
#calcul_1 = fon_t_1.render("Пропущено: ", True, (255, 255, 255)) 
game = True
win = display.set_mode((700, 700))
rock = Player(65, 65, "rocket.png", 315, 620, 4)
#how_ammo = fon_t.render("Всего пуль: " + str(rock.ammo), True, (0, 255, 100))
enemys = sprite.Group()
asteroids = sprite.Group()
for i in range(0, 5):
    enemy = Enemy(65, 65, "ufo.png", randint(5, 650), randint(-50, -10), randint(1, 6))
    enemys.add(enemy)
for i in range(3):
    asteroids.add(Asteroid(65, 65, "asteroid.png", randint(5, 650), randint(-50, -10), randint(2, 5)))
back = transform.scale(image.load("galaxy.jpg"), (700, 700))
clock = time.Clock()
balets = sprite.Group()
#start = vr.time()
amm_i = 5
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if amm_i <= 0:
                    #flagik = True
                    pass
                else:
                    rock.fire()

                    amm_i -= 1
            
    if ((rock.life_flag == False) or (number == 11) or (number_1 == 4)) == False:
        win.blit(back, (0, 0))
        if amm_i <= 0 and rock.reloadam == False:
            rock.reloadam = True
            start = vr.time()
           
        
        if rock.reloadam:
            end = vr.time()
            time_reload = fon_t.render("Перезарядка: " + str(round(SEC - (end - start), 2)), True, (255, 0, 0))
            if round(SEC - (end - start)) <= 0:
                #start = vr.time()
                rock.reloadam = False
                amm_i = 5
        else:
            time_reload = fon_t.render("Заряжено", True, (0, 255, 100))
           
        balets.update()
        balets.draw(win)
        rock.update()
        asteroids.update()
        asteroids.draw(win)
        enemys.update()
    
        enemys.draw(win)
    
        rock.reset()
        for i in enemys:
            if sprite.collide_rect(rock, i):
                
                i.rect.x = randint(5, 650)
                i.rect.y = randint(-50, -10)
                i.speed = randint(1, 6)
                #LIFE-=2
                #if LIFE == 0:
                rock.life_flag = False
            for ha in asteroids:
                if sprite.collide_rect(i, ha):
                    i.rect.x = randint(5, 650)
                    i.rect.y = randint(-50, -10)
                    i.speed = randint(1, 6)
                if sprite.collide_rect(ha, rock):
                   # LIFE-=2
                    #if LIFE == 0:
                    rock.life_flag = False
                    
                for s in balets:
        
        
                    if sprite.collide_rect(i, s):
                
                        number += 1
                        i.rect.x = randint(5, 650)
                        i.rect.y = randint(-50, -10)
                        i.speed = randint(1, 6)
                        s.kill()
            
            
            
                    if sprite.collide_rect(s, ha):
                        s.kill()
        # if LIFE == 2 or LIFE == 3:
        #     life = fon_t.render("Жизнь: "+str(LIFE*25), True, (0, 255, 100))  
        # elif LIFE == 1: 
        #     life = fon_t.render("Жизнь: "+str(LIFE*25), True, (255, 0, 100))  
        # elif LIFE == 0:
        #     life = fon_t.render("Жизнь: "+str(LIFE*25), True, (255, 0, 0)) 
        # else:
        #     life = fon_t.render("Жизнь: "+str(LIFE*25), True, (0, 255, 100))
        calcul = fon_t.render("Счёт: "+str(number), True, (255, 255, 255))
        calcul_1 = fon_t_1.render("Пропущено: "+str(number_1), True, (255, 255, 255))
        if (rock.ammo == 0):
            how_ammo = fon_t.render("Всего пуль: " + str(rock.ammo), True, (255, 0, 0))
        elif (rock.ammo < FIRST/4):
            how_ammo = fon_t.render("Всего пуль: " + str(rock.ammo), True, (255, 0, 100))
        elif (rock.ammo <= FIRST/2):
            how_ammo = fon_t.render("Всего пуль: " + str(rock.ammo), True, (255, 215, 0))
        else:
            
            how_ammo = fon_t.render("Всего пуль: " + str(rock.ammo), True, (0, 255, 100)) 
        win.blit(calcul, (5, 10))
        win.blit(calcul_1, (5, 30))
        win.blit(how_ammo, (5, 50))
        win.blit(time_reload, (5, 90))
        #win.blit(life, (5, 10))

        if (amm_i == 0):
            how_ammo_m = fon_t.render("Пуль в магазине: " + str(amm_i), True, (255, 0, 0))
        elif (amm_i > 3):
            how_ammo_m = fon_t.render("Пуль в магазине: " + str(amm_i), True, (0, 255, 100))
        elif (amm_i <= 3):
            how_ammo_m = fon_t.render("Пуль в магазине: " + str(amm_i), True, (255, 215, 0))
        
       
        
        win.blit(how_ammo_m, (5, 70))
    else: 
        if number == 11:
            mess = fon_ti.render("Победа", True, (0, 255, 55))
        else:
            mess = fon_ti.render("Поражение", True, (255, 0, 55))
        win.blit(mess, (270, 350))
    display.update()
    clock.tick(60)