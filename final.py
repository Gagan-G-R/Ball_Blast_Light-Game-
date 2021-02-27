import pygame
pygame.init()

import random


import sys
clock=pygame.time.Clock()



win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")


player_pos=[250,400]
size=50


enemy_list=[]
bullet_list=[]

speed=2

pygame.mixer.music.load("data/Cat-Burglars.mp3") 
pygame.mixer.music.play(-1,0.0)


BG=pygame.image.load("data/BG.jpg")
BG=pygame.transform.scale(BG,(500,500))


CN=pygame.image.load("data/CN.jpg")
CN=pygame.transform.scale(CN,(75,75))

BM=pygame.image.load("data/BM.jpg")
BM=pygame.transform.scale(BM,(75,75))


BT=pygame.image.load("data/BT.jpg")
BT=pygame.transform.scale(BT,(30,30))

myFont=pygame.font.SysFont("monospace",30) 

blast=pygame.mixer.Sound("data/blast.wav")

out=pygame.mixer.Sound("data/22.wav")

loose=pygame.mixer.Sound("data/win.wav")



def drop_enemies(enemy_list):
    delay=random.random()
    if len(enemy_list)<8 and delay<0.2:
        x_pos=random.randrange(0,450,50)
        y_pos=0
        enemy_list.append([x_pos,y_pos])


def draw_enemies_bullets(enemy_list,bullet_list):
    for i in enemy_list:
        #pygame.draw.rect(win,(255,0,0),(i[0],i[1],size,size))
        win.blit(BM, i)
    for i in bullet_list:
        #pygame.draw.circle(win,(0,255,0),[i[0],i[1]],20)
        win.blit(BT, [i[0]+15,i[1]])

def detect_endgame(enemy_list):
    for i in enemy_list:
        if i[1]>=450 :
            loose.play()
            clock.tick(2000)
            return 1


def update_enemy_pos_bullet_pos(enemy_list,bullet_pos):
    for i in enemy_list:
        i[1]+=speed
    for i in bullet_list:
        i[1]-=speed



def detect_coll(bullet_list,enemy_list):
    for i in enemy_list:
        for j in bullet_list:
            p_x=j[0]
            p_y=j[1]
            e_x=i[0]
            e_y=i[1]
            if (e_x>=p_x and e_x<=(p_x+size)) or (p_x>=e_x and p_x<=(e_x+size)):
                if(e_y>=p_y and e_y<=(p_y+size)) or (p_y>e_y and p_y<=(e_y+size)):
                    enemy_list.remove([i[0],i[1]])
                    bullet_list.remove([j[0],j[1]])
                    blast.play()
                    return 1


endgame= False
score=0

while not endgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                if player_pos[0]<=0:
                    player_pos[0]=0
                else:
                    player_pos[0]-=50;
            if event.key == pygame.K_RIGHT:
                
                if player_pos[0]>=450:
                    player_pos[0]=450
                else:
                    player_pos[0]+=50;
            if event.key == pygame.K_SPACE:
                bullet_list.append([player_pos[0],player_pos[1]-30])
            
        


    win.fill((0,0,0))
    win.blit(BG, [0,0])

    drop_enemies(enemy_list)
    

    draw_enemies_bullets(enemy_list,bullet_list)
    
    #pygame.draw.rect(win,(0,0,255),(player_pos[0],player_pos[1],size,size))
    win.blit(CN, player_pos)

    if detect_coll(bullet_list,enemy_list):
        score=score+1

        

    if detect_endgame(enemy_list):
        out.play()
        endgame = True

    text="Score:"+str(score) 
    label=myFont.render(text,1,(255,255,0))
    win.blit(label,(300,450))


    update_enemy_pos_bullet_pos(enemy_list,bullet_list)
    pygame.display.update()


    clock.tick(20)

clock.tick(20000000)
pygame.quit()

