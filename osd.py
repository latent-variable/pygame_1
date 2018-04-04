import pygame
import game


def text_objects(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    text_choice = pygame.font.Font('Assets/DejaVuSans.ttf',22)
    TextSurf, TextRect = text_objects(text, text_choice)
    TextRect.center = ((game.screen_height*0.1),(game.screen_height * 0.1))
    game.Display.blit(TextSurf, TextRect)

def score(score):
    message_display('Score: '+score)
