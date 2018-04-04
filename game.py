import pygame
import os
import random
import particles
import rocket
import events
import osd

#default colors
black = (0,0,0)
skyblue = (0,150,5)
#set up display
Display = pygame.display.set_mode((1280,720))
screen_width, screen_height = Display.get_size()

clock = pygame.time.Clock()
#load assets and transform
pygame.display.set_caption('Race to the Moon')

# f500 = pygame.image.load('Assets/fighter500.png').convert_alpha()
# f500 = pygame.transform.scale(f500,(int(screen_width*.1),int(screen_height*.25)))
# f000 = pygame.image.load('Assets/fighter000.png').convert_alpha()
# f000 = pygame.transform.scale(f000,(int(screen_width*.1),int(screen_height*.25)))




red_planet = pygame.image.load('Assets/red_planet.png').convert_alpha()
red_planet = pygame.transform.scale(red_planet,(100,100))
green_planet = pygame.image.load('Assets/greenplanet.png').convert_alpha()
green_planet = pygame.transform.scale(green_planet,(120,120))

galaxy = pygame.image.load('Assets/galaxy.png').convert_alpha()
galaxy = pygame.transform.scale(galaxy,(200,220))

star_sky = pygame.image.load('Assets/star_sky.jpg').convert()
star_sky = pygame.transform.scale(star_sky,(screen_width,screen_height))

all_sprites = pygame.sprite.Group()
player = rocket.Player()
all_sprites.add(player)


def earth_background(x,screen_change):
    print(screen_change)
    Display.blit(star_sky,(-earth_width/2 - int(x*.005),((-earth_height +screen_height)+screen_change )))



def background(screen_change):
    Display.blit(star_sky,(0,screen_change-screen_height))
    Display.blit(star_sky,(0,screen_change))


def init():
    pygame.init()

def loop():

    x = (screen_width *0.5)
    y = (screen_height * .8)
    screen_change = 0
    star_change = 0
    y_change = 0
    x_change = 0
    lazer_shot = False
    lazers = []
    stars = particles.Gen_stars(-screen_width, 0)
    particles.gen_enemys(y)

    gameExit = False
    while not gameExit:
        #constant illusion of movement
        screen_change += int((screen_height*.002))
        star_change += int((screen_height*.0021))

        #event handeler*********************************************
        x_change, y_change, lazer_shot = events.handeler(x,y,x_change, y_change)

        all_sprites.update(x_change,y_change)

        #effect of speed
        if y < (screen_height*.4):
            screen_change += int((screen_height*.010))
            star_change += int((screen_height*.012))
            y += 1
        else:
            y += y_change

        #bounderies check
        #x,y = events.bounderies_check(x,y,x_change)

        # Infinite background screen
        if screen_change >= screen_height:
            screen_change = 0
            stars+=(particles.Gen_stars(-(screen_height+star_change), -star_change))
        background(screen_change)
        Display.blit(galaxy,(screen_width/4, star_change - 5*screen_height))



        #draw starts
        if len(stars) > 60:
            del stars[0:20]
        for i in range(0,len(stars)):
            particles.draw_stars(stars[i][0] ,stars[i][1] + star_change,stars[i][2])

        Display.blit(red_planet,(screen_width *.2, int(star_change *.8) -screen_height* .8 ))
        Display.blit(green_planet,(screen_width *.8,int(star_change *.811) -screen_height* .2))

        #draw lazers
        if lazer_shot:
            all_sprites.add(rocket.Lazer(player.rect,10))
            lazer_shot = False

        if len(lazers) > 40:
            del lazers[0:20]
        for i in range(0,len(lazers)):
            lazers[i].draw()

        all_sprites.draw(Display)

        #draw score
        osd.score(str(0))
        clock.tick(60)

        pygame.display.flip()
