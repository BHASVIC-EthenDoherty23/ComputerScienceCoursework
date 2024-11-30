import sys

import pygame
from pygame import time
import button
import ships

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
red_cross = pygame.image.load('Images/redCross.png').convert_alpha() # loads the redCross image
green_Ship = pygame.image.load('Images/greenShip.png').convert_alpha() # loads the greenShip image
blue_Ship = pygame.image.load('Images/blueSquare.png').convert_alpha() # loads the blueSquare image
pink_Ship = pygame.image.load('Images/pinkSquare.png').convert_alpha() # loads the pinkSquare image
orange_Ship = pygame.image.load('Images/orangeSquare.png').convert_alpha() # loads the orangeSquare image
yellow_Ship = pygame.image.load('Images/yellowSquare.png').convert_alpha() # loads the yellowSquare image
orange_Circle = pygame.image.load('Images/orangeCircle.png').convert_alpha() # loads the redSquare image

#create buttons using button class
startButton = button.Button(size[0] / 2.5, size[1] * 0.2, start_Button, 450, 150)
settingsButton = button.Button(size[0] / 2.5, size[1] * 0.4, settings_Button, 450, 150)
statisticsButton = button.Button(size[0] / 2.5, size[1] * 0.6, statistics_Button, 450, 150)
exitButton = button.Button(size[0] / 2.5, size[1] * 0.8, exit_Button, 450, 150)
backButton = button.Button(0, 0, back_Button, 600, 200)
easyButton = button.Button(size[0] / 2.5, size[1] * 0.2, easy_Button, 450, 150)
mediumButton = button.Button(size[0] / 2.5, size[1] * 0.4, medium_Button, 450, 150)
hardButton = button.Button(size[0] / 2.5, size[1] * 0.6, hard_Button, 450, 150)

playerGrid = [[grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square]]
enemyGrid = [[grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square]]


for i in range(10):
    for j in range(10):
        playerGrid[i][j] = button.Button(50*i + size[0] / 5, 50*j + size[1]/ 3, grid_Square, 50, 50) #fill in player and enemy grids with buttons
        enemyGrid[i][j] = button.Button(50*i + size[0] / 1.5, 50*j + size[1]/ 3, grid_Square, 50, 50)
currentScene = "mainMenu"  #used so the program knows what screen to display to start with

backStack = list()  #Stack for the back button
timeSinceSceneChange = 0
turn = -1
enemyShip = False

#instantiate a list called friendlyShips
friendlyShips = list()
enemyShips = list()

#friendly ships creation
fs2Ship = ships.Ship(2, green_Ship, "right")
fs2Ship2 = ships.Ship(2, blue_Ship, "right")
fs3Ship = ships.Ship(3, orange_Ship, "right")
fs4Ship = ships.Ship(4, pink_Ship, "right")
fs5Ship = ships.Ship(5, yellow_Ship, "right")

#enemy ships creation
es2Ship = ships.Ship(2, grid_Square, "right")
es2Ship2 = ships.Ship(2, grid_Square, "right")
es3Ship = ships.Ship(3, grid_Square, "right")
es4Ship = ships.Ship(4, grid_Square, "right")
es5Ship = ships.Ship(5, grid_Square, "right")

def shipListsMaker():
    count = len(friendlyShips)
    count2 = len(enemyShips)
    for i in range(count):
        friendlyShips.pop() #clears list
    for i in range(count2):
        enemyShips.pop() #clears list

    #appends created ships to friendlyShips list
    friendlyShips.append(fs2Ship)
    friendlyShips.append(fs2Ship2)
    friendlyShips.append(fs3Ship)
    friendlyShips.append(fs4Ship)
    friendlyShips.append(fs5Ship)

    #appends created ships to enemyShips list
    enemyShips.append(es2Ship)
    enemyShips.append(es2Ship2)
    enemyShips.append(es3Ship)
    enemyShips.append(es4Ship)
    enemyShips.append(es5Ship)


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
        backStack.append(currentScene)
        currentScene = "easyGame"
        shipListsMaker()
        timeSinceSceneChange = time.get_ticks()
    if mediumButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        backStack.append(currentScene)
        currentScene = "mediumGame"
        shipListsMaker()
        timeSinceSceneChange = time.get_ticks()
    if hardButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        backStack.append(currentScene)
        currentScene = "hardGame"
        shipListsMaker()
        timeSinceSceneChange = time.get_ticks()
    return currentScene





def settingsMenuScene(currentScene):
    pass


def statisticsMenuScene(currentScene):
    pass


def easyGameScene(currentScene):
    global backStack, playerGrid
    global timeSinceSceneChange
    global turn
    global ships
    screen.fill(defaultBackgroundColor)
    for row in range(10):
        for column in range(10):
            if playerGrid[row][column].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100: # checks if the individual grid cell has been clicked
                timeSinceSceneChange = time.get_ticks()
                if turn == -1 and not playerGrid[row][column] == grid_Square: # checks if its the ship placing turn and the clicked grid isnt already taken
                    current_ship = friendlyShips.pop() # sets current_ship to the last
                    if current_ship.checkSize(row) and current_ship.getRotation() == "right": # checks if the selected cell is valid to place a ship of that size and direction
                        for k in range(current_ship.getSize()):
                            playerGrid[row + k][column] = button.Button(50 * (row+k) + size[0] / 5, 50 * column + size[1] / 3, current_ship.getImage(), 50, 50) # for loop that changes the image to the current ships image

                    elif current_ship.checkSize(column) and current_ship.getRotation() == "down": # same as prior if statement, but does down instead of right
                        for k in range(current_ship.getSize()):
                            playerGrid[row][column + k] = button.Button(50 * row + size[0] / 5, 50 * (column + k) + size[1] / 3, current_ship.getImage(), 50, 50)

                    else:
                        friendlyShips.append(current_ship) # if the other 2 if statements fail, it reappends the ship to allow the user to retry

                    if len(friendlyShips) == 0:
                        turn = 1 # if there are no more ships to place, the turn changes to 1

            if enemyGrid[row][column].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if turn == 1 and enemyShip:
                    enemyGrid[row][column] = button.Button(50 * row + size[0] / 1.5, 50 * column + size[1] / 3, orange_Circle, 50, 50)
                    turn = 2
                else:
                    enemyGrid[row][column] = button.Button(50 * row + size[0] / 1.5, 50 * column + size[1] / 3, red_cross, 50, 50)
                    turn = 2

            if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                currentScene = backStack.pop()
                for row in range(10):
                    for column in range(10):
                        playerGrid[row][column] = button.Button(50 * row + size[0] / 5, 50 * column + size[1] / 3, grid_Square, 50, 50)

    return currentScene


def mediumGameScene(currentScene):
    global backStack
    global timeSinceSceneChange
    global turn
    global ships
    screen.fill(defaultBackgroundColor)
    for i in range(10):
        for j in range(10):
            if playerGrid[i][j].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if turn == -1:
                    playerGrid[i][j] = button.Button(50*i + size[0] / 5, 50*j + size[1]/ 3, red_cross, 50, 50)
            if enemyGrid[i][j].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if turn == 1 and enemyShip:
                    enemyGrid[i][j] = button.Button(50*i + size[0] / 1.5, 50*j + size[1]/ 3, red_cross, 50, 50)
                if turn == 1 and not enemyShip:
                    enemyGrid[i][j] = button.Button(50*i + size[0] / 1.5, 50*j + size[1]/ 3, orange_Circle, 50, 50)

        if backButton.draw(screen) and  time.get_ticks() - timeSinceSceneChange > 100:
            currentScene = backStack.pop()
            for i in range(10):
                for j in range(10):
                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3, grid_Square, 50, 50)

    return currentScene

def hardGameScene(currentScene):
    global backStack
    global timeSinceSceneChange
    global turn
    global ships
    screen.fill(defaultBackgroundColor)
    for i in range(10):
        for j in range(10):
            if playerGrid[i][j].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if turn == -1:
                    playerGrid[i][j] = button.Button(50*i + size[0] / 5, 50*j + size[1]/ 3, red_cross, 50, 50)

            if enemyGrid[i][j].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if turn == 1 and enemyShip:
                    enemyGrid[i][j] = button.Button(50*i + size[0] / 1.5, 50*j + size[1]/ 3, red_cross, 50, 50)
                if turn == 1 and not enemyShip:
                    enemyGrid[i][j] = button.Button(50*i + size[0] / 1.5, 50*j + size[1]/ 3, orange_Circle, 50, 50)

        if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
            currentScene = backStack.pop()
            for i in range(10):
                for j in range(10):
                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3, grid_Square, 50, 50)

    return currentScene
#game loop
run = True
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
