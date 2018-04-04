import game
import pygame
import rocket

def handeler(x,y,x_change, y_change):

    lazer_shot = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameExit = True
            quit()
            break

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y_change = -int((game.screen_height*.017))

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y_change = int((game.screen_height*.015))

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x_change = -int((game.screen_width*.01))

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = int((game.screen_width*.01))
            if event.key == pygame.K_SPACE:
                lazer_shot = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                y_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0

    return(x_change,y_change,lazer_shot)

#def bounderies_check(x,y,x_change):
