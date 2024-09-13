import pygame
from gamemap import game_map
global game_map
pygame.init()

blocks = []
bullets = []
players = []
loots = []

size = 30
tank_size = 25

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

font = pygame.font.SysFont('arial',45)

lo = 31
w,h = 26*lo,19*lo
game_w,game_h = 1250,850
screen = pygame.display.set_mode((w,h))

class Block(pygame.Rect):
    def __init__(self,x,y,typeblock,img):
        
        super().__init__(x,y,size,size)
        self.img = img
        self.hp = 1
        self.x,self.y = x*size,y*size
        
        self.type = typeblock
    def update(self):
        if self.hp <= 0:
             blocks.remove(self)
        
    def blit(self):
        self.update()
        screen.blit(self.img,(self.x,self.y))

        
class Bullet(pygame.Rect):
    def __init__(self,parent,dx,dy,damage):
        bullets.append(self)
        self.angle = 0
        self.rt_an = 0
        if dx == 10 and dy == 0:
            self.rt_an = 270
        elif dx == 0 and dy == 10:
            self.rt_an = 180
        elif dx == -10 and dy == 0:
            self.rt_an = 90
        elif dx == 0 and dy == -10:
            self.rt_an = 0
        else:pass

        self.a,self.b = 12,25
        if self.angle == 0:  
            self.w,self.h = self.a,self.b
        elif self.angle == 180:
            self.w,self.h = self.a,self.b
        elif self.angle == 90:
            self.w,self.h = self.b,self.a
        elif self.angle == 270:
            self.w,self.h = self.b,self.a
        else:
            pass
        self.img = pygame.image.load('res\\bullet.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        self.rotate_to(self.rt_an)
        self.parent = parent
        if self.angle == 0 or self.angle == 180:
            self.x,self.y = (self.parent.x+self.parent.w//2)-self.w//2,(self.parent.y+self.parent.h//2)-self.h//2
        else:
            self.x,self.y = (self.parent.x+self.parent.w//2),(self.parent.y+self.parent.h//2)-self.h//4
        super().__init__(self.x,self.y,self.w,self.h)
        self.dx,self.dy = dx,dy
        self.damage = damage
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.mapX,self.mapY = self.x//size,self.y//size
        
        if self.x >= w or self.y >= h or self.x + self.w <= 0 or self.y + self.h <= 0:
            bullets.remove(self)
        
        for block in blocks:
            if block.colliderect(self):
                if block.type == 'green':
                    block.hp -= self.damage
                    try:
                        bullets.remove(self)
                    except:
                        pass
                elif block.type == 'brick':
                    try:
                        bullets.remove(self)
                    except:
                        pass
                else:pass
        for player in players:
            if player.colliderect(self) and player != self.parent:
                player.hp -= self.damage
                try:
                    bullets.remove(self)
                except:
                    pass
    def rotate_to(self,angle):
        rotate = (360-self.angle + angle)
        self.angle = angle
        self.img = pygame.transform.rotate(self.img,rotate)            

        
    def draw(self):
        if self.dx == 0 and self.dy == 0:
            bullets.remove(self)
        else:
            screen.blit(self.img,(self.x,self.y))
            #pygame.draw.circle(screen,(255,255,50),(self.x,self.y),self.rad)
        

class Player(pygame.Rect):
    def __init__(self,x,y,img,color):
        players.append(self)
        self.hp = 3
        self.old_hp = self.hp
        super().__init__(x,y,tank_size,tank_size)
        self.x,self.y = x*size,y*size
        self.dir_x,self.dir_y = x,y
        self.dx,self.dy = 0,0
        self.def_x,self.def_y = self.x,self.y
        self.speed = 5
        self.bulletSpeed = 10
        self.timer = 0
        self.delay = 6
        self.angle = 0
        self.bulletDamage = 1
        self.old_x,self.old_y = 0,0
        self.color = color
        self.text_x,self.text_y = 0,25
        self.bang_img = pygame.image.load('res\\bang.png').convert_alpha()
        self.bang_img = pygame.transform.scale(self.bang_img,(self.w,self.h))
        self.sheild_zone_draw = False
        if self.color == blue:
            self.text_x = w/2-90
        if self.color == red:
            self.text_x = w/2+50
        self.sheild_active = False 
    def update(self):
        if self.sheild_active == True:
            self.hp = 3
            self.sheild_zone_draw = True
            
        self.hp_text = font.render("HP:"+str(self.hp),True,self.color)
            
        for block in blocks:
            if block.colliderect(self):
                self.x = self.old_x
                self.y = self.old_y
        else:
            self.old_x,self.old_y = self.x,self.y
        
    def blit(self):
        if self.sheild_zone_draw == True:
            pygame.draw.circle(screen,(100,100,255,40),(self.x+self.w//2,self.y+self.h//2),(self.w//10)*7)
        screen.blit(self.img,(self.x,self.y))
        if self.hp <= 0:
            screen.blit(self.bang_img,(self.x,self.y))
        screen.blit(self.hp_text,(self.text_x,self.text_y))
        self.bulletrefull.draw()
        
    def rotate_to(self,angle):
        rotate = (360-self.angle + angle)
        self.angle = angle
        self.img = pygame.transform.rotate(self.img,rotate)

        
class PlayerNuber1(Player):
    def __init__(self,x,y):
        self.type = 1
        self.string_color = "blue"
        self.bulletrefull = RefullBullets('player1')
        self.img = pygame.image.load('res\\blue_tank.png')
        self.img = pygame.transform.scale(self.img,(tank_size,tank_size))
        super().__init__(x,y,self.img,blue)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_s]:
            self.rotate_to(90)
            self.x += self.speed
            self.dx = self.bulletSpeed
            self.dy = 0   
        if key[pygame.K_a] and not key[pygame.K_d] and not key[pygame.K_w] and not key[pygame.K_s]:
            self.rotate_to(270)
            self.x -= self.speed
            self.dx = -self.bulletSpeed
            self.dy = 0
        if key[pygame.K_s] and not key[pygame.K_a] and not key[pygame.K_w] and not key[pygame.K_d]:
            self.rotate_to(0)
            self.y += self.speed
            self.dy = self.bulletSpeed
            self.dx = 0
                
        if key[pygame.K_w] and not key[pygame.K_a] and not key[pygame.K_d] and not key[pygame.K_s]:
            self.rotate_to(180)
            self.y -= self.speed
            self.dy = -self.bulletSpeed
            self.dx = 0
                
        if key[pygame.K_SPACE] and self.timer == 0:
            Bullet(self,self.dx,self.dy,self.bulletDamage)
            print(self.angle)
            self.timer = 60
            self.bulletrefull.refull()
        if self.timer > 0: self.timer -= 1
        self.bulletrefull.update()
        
class PlayerNuber2(Player):
    def __init__(self,x,y):
        self.type = 2
        self.string_color = "red"
        self.bulletrefull = RefullBullets('player2')
        self.img = pygame.image.load('res\\red_tank.png')
        self.img = pygame.transform.scale(self.img,(tank_size,tank_size))
        super().__init__(x,y,self.img,red)
    def move(self):  
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and not key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
            self.rotate_to(90)
            self.x += self.speed
            self.dx = self.bulletSpeed
            self.dy = 0   
        if key[pygame.K_LEFT]  and not key[pygame.K_RIGHT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
            self.rotate_to(270)
            self.x -= self.speed
            self.dx = -self.bulletSpeed
            self.dy = 0
        if key[pygame.K_DOWN] and not key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_RIGHT]:
            self.rotate_to(0)
            self.y += self.speed
            self.dy = self.bulletSpeed
            self.dx = 0
                
        if key[pygame.K_UP] and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT] and not key[pygame.K_DOWN]:
            self.rotate_to(180)
            self.y -= self.speed
            self.dy = -self.bulletSpeed
            self.dx = 0
            
        if key[pygame.K_l] and self.timer == 0:
            Bullet(self,self.dx,self.dy,self.bulletDamage)
            self.timer = 60
            self.bulletrefull.refull()
        if self.timer > 0: self.timer -= 1
        self.bulletrefull.update()
        self.bulletrefull.draw()


class RefullBullets():
    def __init__(self,parent_side):
        self.parent_side = parent_side
        self.x = 0
        self.y = 0
        self.color = black
        self.level = 0
        self.max_level = 10
        self.w,self.h = 300,40
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.count = 6
        self.first = True
        self.refulling = False
    def update(self):
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        if self.parent_side == 'player1':
            self.color = blue
            self.x, self.y = 25,25
        if self.parent_side == 'player2':
            self.color = red
            self.x, self.y = w - self.w-25,25
        if self.w >= 360:
            self.first = True
            self.refulling = False
        if self.refulling:
            if self.parent_side == 'player1':
                self.w += self.count
            if self.parent_side == 'player2':
                self.x += self.count
                self.w += self.count
    def refull(self):
        self.refulling = True
        if self.first:
            if self.parent_side == 'player1':
                self.w = 0
            if self.parent_side == 'player2':
                self.x = w - self.w-25
                self.w = 0
        self.first = False
        
    def draw(self):
        if self.parent_side == 'player2':
            pygame.draw.rect(screen,white,(w - 360-25-2,self.y-2,364,self.h+4))
        else: 
            pygame.draw.rect(screen,white,(self.x-2,self.y-2,364,self.h+4))
        pygame.draw.rect(screen,self.color,self.rect)

class Loot(pygame.Rect):
    def __init__(self,x,y,loot_type):
        loots.append(self)
        self.x,self.y = x*size,y*size
        self.old_x = self.x
        self.w,self.h = size,size
        super().__init__(self.x,self.y,self.w,self.h)
        self.type = loot_type
        self.timer = 0
        self.player_id = 0
        if self.type == 'heart':
            self.img = pygame.image.load('res\\heart.png').convert_alpha()
        elif self.type == 'sheild':
            self.img = pygame.image.load('res\\sheild.png').convert_alpha()
            self.rev_time = 30*10
        else:
            pass

        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        
    def update(self):
        for i,player in enumerate(players):
            if player.colliderect(self):
                if self.type == 'heart':
                    player.hp = 3
                if self.type == 'sheild':
                    self.player_id = i
                    player.sheild_active = True
                    player.old_hp = player.hp
                self.x = 9999
                self.timer = 30*15
                
        if self.type == 'sheild':
            if self.rev_time > 0:self.rev_time -= 1
            if self.rev_time <= 0:
                players[self.player_id].sheild_active = False
                players[self.player_id].hp = players[self.player_id].old_hp
                players[self.player_id].sheild_zone_draw = False
                self.rev_time = 30*10
                
        if self.timer>0:self.timer-=1
        
        if self.timer <= 0:
            self.x = self.old_x
        
    def blit(self):
        screen.blit(self.img,(self.x,self.y))




