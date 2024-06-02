import pygame
import sys
from classes import *
from gamemap import game_map
global game_map

pygame.init()

rungame = True
FPS = 60

brick_block = pygame.image.load('res\\brick_block.jpg')
brick_block = pygame.transform.scale(brick_block,(size,size))

green_block = pygame.image.load('res\\green_block.jpeg')
green_block = pygame.transform.scale(green_block,(size,size))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

pygame.display.set_caption('panzer game')
clock = pygame.time.Clock()

try:
    file = open('map.txt','r')
    row,col = 0,0
    for line in file:
        for s in line:
            game_map[row][col] = int(s)
            col += 1
            if col >= 26:
                row += 1
                col = 0
    file.close()
except:
    print("FILE ARE NOT GIVENT")

for i,row in enumerate(game_map):
    for j,col in enumerate(row):
        if col == 1:
            blocks.append(Block(j,i,'brick',brick_block))
        elif col == 2:
            blocks.append(Block(j,i,'green',green_block))
        elif col == 3:
            Loot(j,i,'heart')
        elif col == 4:
            Loot(j,i,'sheild')
        else:
            pass


def stop_text(winner,looser):
     return font.render("WINNER:"+winner+"--->"+"LOOSER:"+looser,True,(255,50,255))

    
p1 = PlayerNuber1(2,5)
p2 = PlayerNuber2(16,7)
stop = False
restart_text = font.render("FOR RESTART [R]",True,(255,255,50))
run_first = True
winner = ""
looser = ""

while rungame:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:rungame = False
    screen.fill(black)

    for block in blocks:
        block.blit()
    for bullet in bullets:
        bullet.update()
        bullet.draw()
    for loot in loots:
        loot.update()
        loot.blit()
    for player in players:
        if stop == False:
            player.update()
            player.move()
        if player.hp <= 0:
            stop = True
        player.blit()

    if stop == True:
        if run_first:
            for player in players:
                player.hp_text = font.render("",True,(0,0,0))
                if player.hp > 0:
                    winner = player.string_color
                if player.hp <= 0:
                    looser = player.string_color
            run_first = False
        screen.blit(stop_text(winner,looser),(w/2-250,25))
        screen.blit(restart_text,(w/2-250,75))
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            stop = False
            run_first = True
            for player in players:
                player.hp = 3
                player.x = player.def_x
                player.y = player.def_y

            for loot in loots:
                loot.timer = 0
        
        
    FPS = 30
    
    pygame.display.update()
pygame.quit()


