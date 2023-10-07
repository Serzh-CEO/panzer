from gamemap import game_map
import pygame

pygame.init()

red = (255,0,0)
heart_red = (230,50,50)
green = (0,255,0)
blue = (0,0,255)
sheild_blue = (50,50,255)
white = (255,255,255)
black = (0,0,0)

size = 50

rungame = True
FPS = 60
w,h = 1290,950
game_w,game_h = 1250,850
screen = pygame.display.set_mode((w,h))
saved = False
pygame.display.set_caption('panzer game')
clock = pygame.time.Clock()
set_game_map = game_map
mx,my = pygame.mouse.get_pos()

def draw(mx,my,color):
    for i,block in enumerate(blocks):
        if block.collidepoint((mx,my)):
            colors[i] = color
def delete(mx,my):
    for i,block in enumerate(blocks):
        if block.collidepoint((mx,my)):
            colors[i] = black
def save():
    row_colors = 0
    col_colors = 0
    index_in_colors = 0
    for row_colors in range(19):
        for i in range(index_in_colors,index_in_colors+26):
            if colors[index_in_colors] == black:
                set_game_map[row_colors][col_colors] = 0
            if colors[index_in_colors] == red:
                set_game_map[row_colors][col_colors] = 1
            if colors[index_in_colors] == green:
                set_game_map[row_colors][col_colors] = 2
            if colors[index_in_colors] == heart_red:
                set_game_map[row_colors][col_colors] = 3
            if colors[index_in_colors] == sheild_blue:
                set_game_map[row_colors][col_colors] = 4

            index_in_colors += 1
            col_colors += 1
            
        col_colors = 0

        
    print(set_game_map)
    print("---------------------------------------------------")
    file = open('map.txt','w')
    for row in range(19):
        for col in range(26):
            file.write(str(set_game_map[row][col]))
    file.close()
    

blocks = []
colors = []



try:
    file = open('map.txt','r')
    row,col = 0,0
    for line in file:
        for s in line:
            set_game_map[row][col] = int(s)
            col += 1
            if col >= 26:
                row += 1
                col = 0
    file.close()
except:
    print("FILE ARE NOT GIVENT")

for i,row in enumerate(set_game_map):
    for j,col in enumerate(row):
        blocks.append(pygame.Rect(j*size,i*size,size,size))
        if col == 1:
            colors.append(red)
        elif col == 2:
            colors.append(green)
        elif col == 0:
            colors.append(black)
        elif col == 3:
            colors.append(heart_red)
        elif col == 4:
            colors.append(sheild_blue)  
        else:
            pass

            
block_color = green
while rungame:
    clock.tick(FPS)
    for e in pygame.event.get():
        if saved==False:
            set_game_map = game_map
        if e.type == pygame.QUIT:rungame = False
    screen.fill(black)
    key = pygame.key.get_pressed()
    mx,my = pygame.mouse.get_pos()

                
    for i,block in enumerate(blocks):
        pygame.draw.rect(screen,colors[i],block)

    if key[pygame.K_1]:
        block_color = red
    if key[pygame.K_2]:
        block_color = green
    if key[pygame.K_3]:
        block_color = heart_red
    if key[pygame.K_4]:
        block_color = sheild_blue

        
    if key[pygame.K_d]:
        draw(mx,my,block_color)
    elif key[pygame.K_SPACE]:
        delete(mx,my)
    elif key[pygame.K_s]:
        save()
    else:
        pass
    pygame.display.update()
pygame.quit()









