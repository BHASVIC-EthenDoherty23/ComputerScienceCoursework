import pygame
import button

#initialise pygame and screen
pygame.init()
desktop_size = pygame.display.get_desktop_sizes()
size = desktop_size[0]
screen = pygame.display.set_mode(size)

#load images/backgrounds
defaultBackgroundColor = 27,27,237
start_Button = pygame.image.load('Images/StartButton.png').convert_alpha()
settings_Button = pygame.image.load('Images/settingButton.png').convert_alpha()
statistics_Button = pygame.image.load('Images/statisticButton.png').convert_alpha()
exit_Button = pygame.image.load('Images/ExitButton.png').convert_alpha()



#create buttons using button class
startButton = button.Button(size[0]/2.5 , size[1] * 0.2, start_Button)
settingsButton = button.Button(size[0]/2.5 , size[1] * 0.4, settings_Button)
statisticsButton = button.Button(size[0]/2.5 , size[1] * 0.6, statistics_Button)
exitButton = button.Button(size[0]/2.5 , size[1] * 0.8, exit_Button)

currentScene = "mainMenu"

#Scene creation for swapping through screens
def mainMenuScene():
    background = pygame.draw.rect(screen, defaultBackgroundColor, (0,0,size[0],size[1]), 0)
    if startButton.draw(screen):
        #currentScene = "playMenu"
        print("Start")
    if settingsButton.draw(screen):
        print("Settings")
        #currentScene = "settingsMenu"
    if statisticsButton.draw(screen):
        print("Statistics")
        #currentScene = "statisticsMenu"
    if exitButton.draw(screen):
        print("EXITED")
        #pygame.quit()


def playMenuScene():
    background = pygame.draw.rect(screen, defaultBackgroundColor, (0,0,size[0],size[1]), 0)


#game loop
run = True
while run:
     if currentScene == "mainMenu":
          mainMenuScene()
     elif currentScene == "playMenu":
         playMenuScene()
     pygame.display.update()

pygame.quit()