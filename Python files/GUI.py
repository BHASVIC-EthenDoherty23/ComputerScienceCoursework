import sys

import pygame
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
start_Button = pygame.image.load('Images/StartButton.png')  #loads the StartButton image
settings_Button = pygame.image.load('Images/settingButton.png')  #loads the SettingsButton image
statistics_Button = pygame.image.load('Images/statisticButton.png')  #loads the StatisticsButton image
exit_Button = pygame.image.load('Images/ExitButton.png')  # loads the ExitButton image

#create buttons using button class
startButton = button.Button(size[0] / 2.5, size[1] * 0.2, start_Button)
settingsButton = button.Button(size[0] / 2.5, size[1] * 0.4, settings_Button)
statisticsButton = button.Button(size[0] / 2.5, size[1] * 0.6, statistics_Button)
exitButton = button.Button(size[0] / 2.5, size[1] * 0.8, exit_Button)

currentScene = "mainMenu"  #used so the program knows what screen to display


#Scene creation for swapping through screens
def mainMenuScene():
    background = pygame.draw.rect(screen, defaultBackgroundColor, (0, 0, size[0], size[1]), 0)
    if startButton.draw(screen):  #checks if returned value of clicked is true or false
        currentScene = "playMenu"  #changes scene to the play menu
        print(currentScene)
    elif settingsButton.draw(screen):  #checks if returned value of clicked is true or false
        currentScene = "settingsMenu"  #changes scene to the play menu
        print(currentScene)
    elif statisticsButton.draw(screen):  #checks if returned value of clicked is true or false
        currentScene = "statisticsMenu"  #changes scene to the play menu
        print(currentScene)
    elif exitButton.draw(screen):
        pygame.quit()


def playMenuScene():
    screen.fill(defaultBackgroundColor)


#game loop
run = True
while run:
    if currentScene == "mainMenu":
        mainMenuScene()
    elif currentScene == "playMenu":
        playMenuScene()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
