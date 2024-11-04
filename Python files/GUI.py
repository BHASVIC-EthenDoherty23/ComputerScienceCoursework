import sys

import pygame
from pygame import time

import button

#initialise pygame and screen
pygame.init()
desktop_size = pygame.display.get_desktop_sizes()  #returns an array of sizes of all of the users monitors
size = desktop_size[0]  #gets the first monitors size from the array
pygame.display.set_caption("Battleships Against Computer")  #sets name of program to Battleships Against Computer
pygame.time.Clock().tick(60)  #sets max framerate to 60
screen = pygame.display.set_mode(size)

#load images/backgrounds
defaultBackgroundColor = 27, 27, 237  #Dark Blue like the ocean
start_Button = pygame.image.load('Images/StartButton.png').convert_alpha()  #loads the StartButton image
settings_Button = pygame.image.load('Images/settingButton.png').convert_alpha()  #loads the SettingsButton image
statistics_Button = pygame.image.load('Images/statisticButton.png').convert_alpha()  #loads the StatisticsButton image
exit_Button = pygame.image.load('Images/ExitButton.png').convert_alpha()  # loads the ExitButton image
back_Button = pygame.image.load('Images/back.png').convert_alpha()  #loads the back button image
easy_Button = pygame.image.load('Images/EasyButton.png').convert_alpha()  #loads the EasyButton image
medium_Button = pygame.image.load('Images/MediumButton.png').convert_alpha()  #loads the MediumButton image
hard_Button = pygame.image.load('Images/HardButton.png').convert_alpha()  #loads the HardButton image
grid_Square = pygame.image.load('Images/gridSquare.png').convert_alpha() # loads the gridSquare image

#create buttons using button class
startButton = button.Button(size[0] / 2.5, size[1] * 0.2, start_Button, 150)
settingsButton = button.Button(size[0] / 2.5, size[1] * 0.4, settings_Button, 150)
statisticsButton = button.Button(size[0] / 2.5, size[1] * 0.6, statistics_Button, 150)
exitButton = button.Button(size[0] / 2.5, size[1] * 0.8, exit_Button, 150)
backButton = button.Button(0, 0, back_Button, 200)
easyButton = button.Button(size[0] / 2.5, size[1] * 0.2, easy_Button, 150)
mediumButton = button.Button(size[0] / 2.5, size[1] * 0.4, medium_Button, 150)
hardButton = button.Button(size[0] / 2.5, size[1] * 0.6, hard_Button, 150)
currentScene = "mainMenu"  #used so the program knows what screen to display to start with

backStack = list()  #Stack for the back button
timeSinceSceneChange = 0

#Scene creation for swapping through screens
def mainMenuScene(currentScene):
    global backStack
    global timeSinceSceneChange
    background = pygame.draw.rect(screen, defaultBackgroundColor, (0, 0, size[0], size[1]), 0)
    if startButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:  #checks if returned value of clicked is true or false
        backStack.append(currentScene)  # pushes the current scene onto the top of the stack
        currentScene = "playMenu"  #changes scene to the play menu
        print(currentScene)
        timeSinceSceneChange = time.get_ticks() #set current time in milliseconds to the variable "timeSinceSceneChange"
    elif settingsButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:  #checks if returned value of clicked is true or false
        currentScene = "settingsMenu"  #changes scene to the play menu
        print(currentScene)
        timeSinceSceneChange = time.get_ticks()
    elif statisticsButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:  #checks if returned value of clicked is true or false
        currentScene = "statisticsMenu"  #changes scene to the play menu
        print(currentScene)
        timeSinceSceneChange = time.get_ticks()
    elif exitButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        pygame.quit()

    return currentScene


def playMenuScene(currentScene):
    global backStack
    global timeSinceSceneChange
    screen.fill(defaultBackgroundColor)  # fills screen to remove all old scene
    if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = backStack.pop()
    if easyButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = "easyGame"
        timeSinceSceneChange = time.get_ticks()
    if mediumButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = "mediumGame"
        timeSinceSceneChange = time.get_ticks()
    if hardButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = "hardGame"
        timeSinceSceneChange = time.get_ticks()
    return currentScene


#game loop
run = True


def settingsMenuScene(currentScene):
    pass


def statisticsMenuScene(currentScene):
    pass


def easyGameScene(currentScene):
    pass



def mediumGameScene(currentScene):
    pass


def hardGameScene(currentScene):
    pass


while run:
    print(backStack, "back stack")
    if currentScene == "mainMenu":
        print(currentScene)
        currentScene = mainMenuScene(currentScene)
    elif currentScene == "playMenu":
        print(currentScene)
        currentScene = playMenuScene(currentScene)
    elif currentScene == "settingsMenu":
        print(currentScene)
        currentScene = settingsMenuScene(currentScene)
    elif currentScene == "statisticsMenu":
        print(currentScene)
        currentScene == statisticsMenuScene(currentScene)
    elif currentScene == "easyGame":
        print(currentScene)
        currentScene = easyGameScene(currentScene)
    elif currentScene == "mediumGame":
        print(currentScene)
        currentScene = mediumGameScene(currentScene)
    elif currentScene == "hardGame":
        print(currentScene)
        currentScene = hardGameScene(currentScene)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
