import game
import pygame
import events


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageCenter = pygame.image.load('Assets/fighter000.png').convert_alpha()
        self.imageCenter = pygame.transform.scale(self.imageCenter,(int(game.screen_width*.1),int(game.screen_height*.25)))
        self.imageRight = pygame.image.load('Assets/fighter005.png').convert_alpha()
        self.imageRight = pygame.transform.scale(self.imageRight,(int(game.screen_width*.1),int(game.screen_height*.25)))
        self.imageLeft = pygame.image.load('Assets/fighter500.png').convert_alpha()
        self.imageLeft = pygame.transform.scale(self.imageLeft,(int(game.screen_width*.1),int(game.screen_height*.25)))
        self.image = self.imageCenter
        self.rect = self.image.get_rect()
        self.rect.center = (game.screen_width *0.5, game.screen_height * .8)

    def update(self,x_change, y_change):
        if x_change > 0 :
            self.image = self.imageRight
        elif x_change < 0:
            self.image = self.imageLeft
        else:
            self.image = self.imageCenter
        if self.rect.right > game.screen_width:
            self.rect.right = game.screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        # else:
        #     self.rect.x += x_change
        # if self.rect.top < (game.screen_height*.4):
        #     self.rect.top =  (game.screen_height*.4)
        # if self.rect.bottom > 0:
        #     self.rect.bottom = 0
        # else:
        #     self.rect.y += y_change
        #self.rect.x,self.rect.y = events.bounderies_check(self.rect.x,self.rect.y,x_change)


class Lazer(pygame.sprite.Sprite):

    def __init__(self,rect, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.color = (100,200,255)
        self.image =pygame.Surface((2,15))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (rect.x + rect.width/2,rect.y)

    def update(self,x_temp,y_temp):
        self.rect.y -= self.speed


class Ares(pygame.sprite.Sprite):
    def __init__(self, x , y ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/ares.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,70))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 2

    def update(self,x_change,y_change):
        self.rect.y += self.speed - y_change
