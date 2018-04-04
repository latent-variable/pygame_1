import game
import pygame
import random
import rocket



def Gen_stars(posy0,posy1):
    stars = []
    star = []
    for x in range(0,20):
        star= [random.randrange(0,game.screen_width),random.randrange(posy0,posy1),random.randrange(1,int(game.screen_width*.0023))]
        stars.append(star)
    return stars


def draw_stars(posx,posy,size):
    starcolor = (255,255,155)
    pygame.draw.circle(game.Display,starcolor,(posx,posy),size)


def gen_astros():
    pass

def gen_enemys(y):
    for i in range(0,10):
        enemy = rocket.Ares((random.randrange(100,game.screen_width-100)),-(random.randrange(2*game.screen_height, 10*game.screen_height)))
        game.all_sprites.add(enemy)
