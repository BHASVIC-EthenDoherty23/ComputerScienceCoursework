import time
from email.policy import default

import pygame

pygame.init()
desktop_size = pygame.display.get_desktop_sizes()
size = desktop_size[0]
screen = pygame.display.set_mode(size)

defaultBackgroundColor = 27,27,237
defaultBoxColour = 223,223,252

currentScene = ""

def mainMenuDisplayer():
    background = pygame.draw.rect(screen, defaultBackgroundColor, (0,0,size[0],size[1]), 0)
    playButton = pygame.draw.rect(screen, defaultBoxColour , (size[0]/2.5 , size[1] * 0.2 , size[0]/4 , size[1]/10), 0 )
    settingsButton = pygame.draw.rect(screen, defaultBoxColour , (size[0]/2.5 , size[1] * 0.4 , size[0]/4 , size[1]/10), 0 )
    statisticsButton = pygame.draw.rect(screen, defaultBoxColour , (size[0]/2.5 , size[1] * 0.6 , size[0]/4 , size[1]/10),  0 )
    quitButton = pygame.draw.rect(screen, defaultBoxColour,  (size[0]/2.5 , size[1] * 0.8 , size[0]/4 , size[1]/10), 0 )
    currentScene = "mainMenu"

mainMenuDisplayer()
pygame.display.flip()

time.sleep(60)