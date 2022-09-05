import sys

import pygame
import random
import timing_mechanics

pygame.init()

fps = 20
fpsClock = pygame.time.Clock()
garbage_bag = pygame.image.load('images/poo.png')
bug = pygame.image.load('images/bug.png')
trucc = [pygame.image.load('images/trucc.png'), pygame.image.load('images/truccL.png')]
width, height = 360, 420
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('images/Gamebg.png')
location = 140
flip = 0
points = 0
itemsarr = []
index_pop = []
start_time = pygame.time.get_ticks()
temp_len = 0
prev_time = 0
life_count = 3
lose_page = pygame.image.load('images/losePage.png')
heart = pygame.image.load('images/heartIMG.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (location > 0):
                    location -= 20
                flip = 1
            if event.key == pygame.K_RIGHT:
                if (location < 275):
                    location += 20
                flip = 0

    screen.blit(bg, (0, 0))
    screen.blit(trucc[flip], (location, 335))
    curr_time = pygame.time.get_ticks()-start_time
    temp_len = len(itemsarr)
    itemsarr = timing_mechanics.track_objects(itemsarr,curr_time,prev_time)
    if(temp_len < len(itemsarr)):
        prev_time = curr_time
    for i in range(0,len(itemsarr)-1):
        itemsarr[i][2] = itemsarr[i][2] + 10
        if (itemsarr[i][2] >= 310 and itemsarr[i][1] >= location and itemsarr[i][1] <=(location + 80)):
            if(itemsarr[i][0] == ['images/poo.png']):
                points = points + 1
            else:
                life_count = life_count - 1
                if (life_count < 1):
                    screen.blit(lose_page,(0, 0))
                    font = pygame.font.Font(pygame.font.get_default_font(), 40)
                    points_surface = font.render("Score: " + str(points), True, (0,0,0))

                    screen.blit(points_surface, (150, 225))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pygame.quit()
                    sys.exit()
            itemsarr[i][2] = -40
            index_pop.append(i)
        elif (itemsarr[i][2] >= 340):
            if(itemsarr[i][0] == ['images/poo.png']):
                points = points - 1
            itemsarr[i][2] = -40
            index_pop.append(i)
        if (itemsarr[i][0] == ['images/poo.png']):
            screen.blit(garbage_bag,(itemsarr[i][1],itemsarr[i][2]))
        else:
            screen.blit(bug,(itemsarr[i][1],itemsarr[i][2]))
    for i in range(0,life_count):
        screen.blit(heart,(250+(i*30),370))            
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    points_surface = font.render(str(points), True, (255, 255, 255))
    screen.blit(points_surface, (50, 370))
    pygame.display.update()
    for index in index_pop:
        itemsarr.pop(index)
    index_pop = []
    pygame.display.flip()
    fpsClock.tick(fps)
