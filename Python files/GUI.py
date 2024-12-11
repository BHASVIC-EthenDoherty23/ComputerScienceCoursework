import sys
from random import random

import pygame
from numpy.random import random_integers
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
settings_Button = pygame.image.load('Images/SettingsButton.png').convert_alpha()  #loads the SettingsButton image
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
orange_Circle = pygame.image.load('Images/orangeCircle.png').convert_alpha() # loads the orange_Circle image
attacked_Ship = pygame.image.load('Images/attackedShip.png').convert_alpha() # loads the attackedShip image
main_Title = pygame.image.load('Images/mainTitle.png').convert_alpha() # loads the mainTitle image
select_Difficulty = pygame.image.load('Images/selectDifficulty.png').convert_alpha()
rotation_Button = pygame.image.load('Images/rotationButton.png').convert_alpha()
black_Square = pygame.image.load('Images/blackSquare.png').convert_alpha()

#create buttons using button class
startButton = button.Button(size[0] / 2.5, size[1] * 0.2, start_Button, 450, 150)
settingsButton = button.Button(size[0] / 2.5, size[1] * 0.4, settings_Button, 450, 150)
statisticsButton = button.Button(size[0] / 2.5, size[1] * 0.6, statistics_Button, 450, 150)
exitButton = button.Button(size[0] / 2.5, size[1] * 0.8, exit_Button, 450, 150)
backButton = button.Button(0, 0, back_Button, 600, 200)
easyButton = button.Button(size[0] / 2.5, size[1] * 0.2, easy_Button, 450, 150)
mediumButton = button.Button(size[0] / 2.5, size[1] * 0.4, medium_Button, 450, 150)
hardButton = button.Button(size[0] / 2.5, size[1] * 0.6, hard_Button, 450, 150)
mainTitle = button.Button(size[0] /2.7, size[1] * 0.02, main_Title, 600, 200)
selectDifficulty = button.Button(size[0] /2.7, size[1] * 0.02, select_Difficulty, 600, 200)
rotationButton = button.Button(size[0] / 4, size[1] * 0.02, rotation_Button, 600, 200)

tempPlayerGrid = [[grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square]]
tempEnemyGrid = [[grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square]]
playerGrid = [[grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square]]
enemyGrid = [[grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square], [grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square, grid_Square]]
playerShipStorer = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
enemyShipStorer = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]


for i in range(10):
    for j in range(10):
        tempPlayerGrid[i][j] = button.Button(50*i + size[0] / 5, 50*j + size[1]/ 3, grid_Square, 50, 50) #fill in player and enemy grids with buttons
        tempEnemyGrid[i][j] = button.Button(50*i + size[0] / 1.5, 50*j + size[1]/ 3, grid_Square, 50, 50)
        playerGrid[i][j] = tempPlayerGrid[i][j] #Sets the playerGrid and enemyGrid to the same as the temp grid
        enemyGrid[i][j] = tempEnemyGrid[i][j]

currentScene = "mainMenu"  #used so the program knows what screen to display to start with

backStack = list()  #Stack for the back button
timeSinceSceneChange = time.get_ticks()
turn = -1 # Place ships phase
enemyShip = False
chosenAttacks = list() # lists so that player and computer cant repeat moves
chosenAttacksPlayer = list()
#instantiate a list called friendlyShips and enemyShips
friendlyShips = list()
enemyShips = list()
direction = "right"

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

def resetShipLists():
    #appends created ships to friendlyShips and enemyShips list after removing all elements of the friendlyShips and enemyShips lists
    for i in range(len(friendlyShips)):
        friendlyShips.pop()
    for i in range(len(enemyShips)):
        enemyShips.pop()
    friendlyShips.append(fs2Ship)
    friendlyShips.append(fs2Ship2)
    friendlyShips.append(fs3Ship)
    friendlyShips.append(fs4Ship)
    friendlyShips.append(fs5Ship)


    enemyShips.append(es2Ship)
    enemyShips.append(es2Ship2)
    enemyShips.append(es3Ship)
    enemyShips.append(es4Ship)
    enemyShips.append(es5Ship)

    playerShipStorer = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    enemyShipStorer = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #Resets both lists so that the player and computer can attack in new games
    for i in range(len(chosenAttacks)):
        chosenAttacks.pop()
    for i in range(len(chosenAttacksPlayer)):
        chosenAttacksPlayer.pop()

resetShipLists()

#Scene creation for swapping through screens
def mainMenuScene(currentScene):
    global backStack
    global timeSinceSceneChange
    background = pygame.draw.rect(screen, defaultBackgroundColor, (0, 0, size[0], size[1]), 0)
    mainTitle.draw(screen)
    if startButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:  #checks if returned value of clicked is true or false
        backStack.append(currentScene)  # pushes the current scene onto the top of the stack
        currentScene = "playMenu"  #changes scene to the play menu
        print(currentScene)
        timeSinceSceneChange = time.get_ticks() #set current time in milliseconds to the variable "timeSinceSceneChange"
    elif settingsButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:  #checks if returned value of clicked is true or false
        backStack.append(currentScene)
        currentScene = "settingsMenu"  #changes scene to the play menu
        print(currentScene)
        timeSinceSceneChange = time.get_ticks()
    elif statisticsButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:  #checks if returned value of clicked is true or false
        backStack.append(currentScene)
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
    selectDifficulty.draw(screen)
    if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = backStack.pop()
    if easyButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        backStack.append(currentScene)
        currentScene = "easyGame"
        timeSinceSceneChange = time.get_ticks()
    if mediumButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        backStack.append(currentScene)
        currentScene = "mediumGame"
        timeSinceSceneChange = time.get_ticks()
    if hardButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        backStack.append(currentScene)
        currentScene = "hardGame"
        timeSinceSceneChange = time.get_ticks()
    return currentScene





def settingsMenuScene(currentScene):
    screen.fill(defaultBackgroundColor)
    global backStack
    global timeSinceSceneChange
    screen.fill(defaultBackgroundColor)  # fills screen to remove all old scene
    if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = backStack.pop()
    return currentScene


def statisticsMenuScene(currentScene):
    screen.fill(defaultBackgroundColor)
    global backStack
    global timeSinceSceneChange
    screen.fill(defaultBackgroundColor)  # fills screen to remove all old scene
    if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
        currentScene = backStack.pop()
    return currentScene


def easyGameScene(currentScene):
    global backStack, playerGrid
    global timeSinceSceneChange
    global turn
    global direction
    screen.fill(defaultBackgroundColor)
    for row in range(10):
        for column in range(10):
            if turn == -1 and rotationButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if direction == "right":
                    direction = "down"
                else:
                    direction = "right"
            if playerGrid[row][column].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100: # checks if the individual grid cell has been clicked
                timeSinceSceneChange = time.get_ticks()
                if turn == -1: # checks if its the ship placing turn
                    current_ship = friendlyShips.pop() # sets current_ship to the last
                    shipNum = len(friendlyShips) + 1
                    if current_ship.checkSize(row-1) and direction == "right": # checks if the selected cell is valid to place a ship of that size and direction
                        overridesShip = False
                        for k in range(current_ship.getSize()):
                            if not playerGrid[row + k][column] == tempPlayerGrid[row + k][column]:
                                overridesShip = True
                        if not overridesShip:
                            for k in range(current_ship.getSize()):
                                playerGrid[row + k][column] = button.Button(50 * (row+k) + size[0] / 5, 50 * column + size[1] / 3, current_ship.getImage(), 50, 50) # for loop that changes the image to the current ships image
                                playerShipStorer[row + k][column] = shipNum
                        else:
                            friendlyShips.append(current_ship)
                    elif current_ship.checkSize(column-1) and direction == "down": # same as prior if but does down instead of right
                        overridesShip = False
                        for k in range(current_ship.getSize()):
                            if not playerGrid[row][column + k] == tempPlayerGrid[row][column + k]:
                                overridesShip = True
                        if not overridesShip:
                            for k in range(current_ship.getSize()):
                                playerGrid[row][column + k] = button.Button(50 * row + size[0] / 5, 50 * (column + k) + size[1] / 3, current_ship.getImage(), 50,50)  # for loop that changes the image to the current ships image
                                playerShipStorer[row][column + k] = shipNum
                        else:
                            friendlyShips.append(current_ship)
                    else:
                       friendlyShips.append(current_ship)
                    if len(friendlyShips) == 0:
                        turn = 0  # if there are no more ships to place, the turn changes to 1

            if turn == 0:
                current_ship = enemyShips.pop()

                randomRow = random_integers(0, 9)
                randomColumn = random_integers(0, 9)
                randomDirection = random_integers(0, 1)
                shipNum = len(enemyShips) + 1
                if randomDirection == 0:
                    direction = "down"
                else:
                    direction = "right"

                if current_ship.checkSize(randomRow - 1) and direction == "right":  # checks if the selected cell is valid to place a ship of that size and direction
                    timeSinceSceneChange = time.get_ticks()
                    overridesShip = False
                    for k in range(current_ship.getSize()):
                        if not enemyGrid[randomRow + k][randomColumn] == tempEnemyGrid[randomRow + k][randomColumn]:
                            overridesShip = True
                    if not overridesShip:
                        for k in range(current_ship.getSize()):
                            enemyGrid[randomRow + k][randomColumn] = button.Button(50 * (randomRow + k) + size[0] / 1.5, 50 * randomColumn + size[1] / 3, grid_Square, 50,50)  # for loop that changes the image to the current ships image
                            enemyShipStorer[randomRow + k][randomColumn] = shipNum
                    else:
                        enemyShips.append(current_ship)
                elif current_ship.checkSize(randomColumn) and direction == "down":  # same as prior if, but does down instead of right
                    overridesShip = False
                    for k in range(current_ship.getSize()):
                        if not enemyGrid[randomRow][randomColumn + k] == tempEnemyGrid[randomRow][randomColumn + k]:
                            overridesShip = True
                    if not overridesShip:
                        for k in range(current_ship.getSize()):
                            enemyGrid[randomRow][randomColumn + k] = button.Button(50 * randomRow + size[0] / 1.5, 50 * (randomColumn + k) + size[1] / 3, grid_Square, 50,50)  # for loop that changes the image to the current ships image
                            enemyShipStorer[randomRow][randomColumn + k] = shipNum
                    else:
                        enemyShips.append(current_ship)

                else:
                    enemyShips.append(current_ship)  # if the other 2 if statements fail, it reappends the ship to allow the user to retry
                if len(enemyShips) == 0:
                    turn = 1
            if enemyGrid[row][column].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100 and turn == 1:
                isAttackablePlayer = True
                timeSinceSceneChange = time.get_ticks()
                for i in range(len(chosenAttacksPlayer)):
                    if chosenAttacksPlayer[i] == (row,column):
                        isAttackablePlayer = False

                if isAttackablePlayer:
                    chosenAttacksPlayer.append((row,column))

                if enemyGrid[row][column] != tempEnemyGrid[row][column] and isAttackablePlayer:
                    enemyGrid[row][column] = button.Button(50 * row + size[0] / 1.5, 50 * column + size[1] / 3, orange_Circle, 50, 50)
                    enemyShipStorer[row][column] += 10
                    turn = 2
                    counter5L = 0
                    counter4L = 0
                    counter3L = 0
                    counter2L = 0
                    counter2L2 = 0
                    for i in range(10):
                        for j in range(10):
                            if enemyShipStorer[i][j] == 15:
                                counter5L += 1
                            elif enemyShipStorer[i][j] == 14:
                                counter4L += 1
                            elif enemyShipStorer[i][j] == 13:
                                counter3L += 1
                            elif enemyShipStorer[i][j] == 12:
                                counter2L += 1
                            elif enemyShipStorer[i][j] == 11:
                                counter2L2 += 1
                    if counter5L == 5:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 15:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter4L == 4:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 14:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter3L == 3:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 13:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter2L == 2:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 12:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter2L2 == 2:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 11:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                elif enemyGrid[row][column] == tempEnemyGrid[row][column] and isAttackablePlayer:
                    enemyGrid[row][column] = button.Button(50 * row + size[0] / 1.5, 50 * column + size[1] / 3, red_cross, 50, 50)
                    turn = 2
                timeSinceSceneChange = time.get_ticks()
            if turn == 2 and time.get_ticks() - timeSinceSceneChange > 1000:
                isAttackable = True
                randomRow = random_integers(0, 9)
                randomColumn = random_integers(0, 9)
                for i in range(len(chosenAttacks)):
                    if chosenAttacks[i] == (randomRow, randomColumn):
                        isAttackable = False
                if isAttackable:
                    chosenAttacks.append((randomRow, randomColumn))

                if playerGrid[randomRow][randomColumn] != tempPlayerGrid[randomRow][randomColumn] and isAttackable:
                    playerGrid[randomRow][randomColumn] = button.Button(50 * randomRow + size[0] / 5, 50 * randomColumn + size[1] / 3, attacked_Ship , 50,50)
                    turn = 1
                    timeSinceSceneChange = time.get_ticks()
                    playerShipStorer[randomRow][randomColumn] += 10
                    counter5L = 0
                    counter4L = 0
                    counter3L = 0
                    counter2L = 0
                    counter2L2 = 0
                    for i in range(10):
                        for j in range(10):
                            if playerShipStorer[i][j] == 15:
                                counter5L += 1
                            elif playerShipStorer[i][j] == 14:
                                counter4L += 1
                            elif playerShipStorer[i][j] == 13:
                                counter3L += 1
                            elif playerShipStorer[i][j] == 12:
                                counter2L += 1
                            elif playerShipStorer[i][j] == 11:
                                counter2L2 += 1
                    if counter5L == 5:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 15:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                    black_Square, 50, 50)
                    if counter4L == 4:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 14:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                    black_Square, 50, 50)
                    if counter3L == 3:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 13:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                    black_Square, 50, 50)
                    if counter2L == 2:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 12:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                    black_Square, 50, 50)
                    if counter2L2 == 2:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 11:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                    black_Square, 50, 50)

                elif playerGrid[randomRow][randomColumn] == tempPlayerGrid[randomRow][randomColumn] and isAttackable:
                    playerGrid[randomRow][randomColumn] = button.Button(50 * randomRow + size[0] / 5, 50 * randomColumn + size[1] / 3, red_cross, 50,50)
                    turn = 1
                    timeSinceSceneChange = time.get_ticks()
        if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
            currentScene = backStack.pop()
            turn = -1
            resetShipLists()
            for row in range(10):
                for column in range(10):
                    playerGrid[row][column] = tempPlayerGrid[row][column]
                    enemyGrid[row][column] = tempEnemyGrid[row][column]
            timeSinceSceneChange = time.get_ticks()

    return currentScene


def mediumGameScene(currentScene):
    global backStack, playerGrid
    global timeSinceSceneChange
    global turn
    global direction
    screen.fill(defaultBackgroundColor)
    for row in range(10):
        for column in range(10):
            if turn == -1 and rotationButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
                if direction == "right":
                    direction = "down"
                else:
                    direction = "right"
            if playerGrid[row][column].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100: # checks if the individual grid cell has been clicked
                timeSinceSceneChange = time.get_ticks()
                if turn == -1: # checks if its the ship placing turn
                    current_ship = friendlyShips.pop() # sets current_ship to the last
                    shipNum = len(friendlyShips) + 1
                    if current_ship.checkSize(row-1) and direction == "right": # checks if the selected cell is valid to place a ship of that size and direction
                        overridesShip = False
                        for k in range(current_ship.getSize()):
                            if not playerGrid[row + k][column] == tempPlayerGrid[row + k][column]:
                                overridesShip = True
                        if not overridesShip:
                            for k in range(current_ship.getSize()):
                                playerGrid[row + k][column] = button.Button(50 * (row+k) + size[0] / 5, 50 * column + size[1] / 3, current_ship.getImage(), 50, 50) # for loop that changes the image to the current ships image
                                playerShipStorer[row + k][column] = shipNum
                        else:
                            friendlyShips.append(current_ship)
                    elif current_ship.checkSize(column-1) and direction == "down": # same as prior if but does down instead of right
                        overridesShip = False
                        for k in range(current_ship.getSize()):
                            if not playerGrid[row][column + k] == tempPlayerGrid[row][column + k]:
                                overridesShip = True
                        if not overridesShip:
                            for k in range(current_ship.getSize()):
                                playerGrid[row][column + k] = button.Button(50 * row + size[0] / 5, 50 * (column + k) + size[1] / 3, current_ship.getImage(), 50,50)  # for loop that changes the image to the current ships image
                                playerShipStorer[row][column + k] = shipNum
                        else:
                            friendlyShips.append(current_ship)
                    else:
                        friendlyShips.append(current_ship)
                    if len(friendlyShips) == 0:
                        turn = 0  # if there are no more ships to place, the turn changes to 1

            if turn == 0:
                current_ship = enemyShips.pop()

                randomRow = random_integers(0, 9)
                randomColumn = random_integers(0, 9)
                randomDirection = random_integers(0, 1)
                shipNum = len(enemyShips) + 1
                if randomDirection == 0:
                    direction = "down"
                else:
                    direction = "right"

                if current_ship.checkSize(randomRow - 1) and direction == "right":  # checks if the selected cell is valid to place a ship of that size and direction
                    timeSinceSceneChange = time.get_ticks()
                    overridesShip = False
                    for k in range(current_ship.getSize()):
                        if not enemyGrid[randomRow + k][randomColumn] == tempEnemyGrid[randomRow + k][randomColumn]:
                            overridesShip = True
                    if not overridesShip:
                        for k in range(current_ship.getSize()):
                            enemyGrid[randomRow + k][randomColumn] = button.Button(50 * (randomRow + k) + size[0] / 1.5, 50 * randomColumn + size[1] / 3, grid_Square, 50,50)  # for loop that changes the image to the current ships image
                            enemyShipStorer[randomRow + k][randomColumn] = shipNum
                    else:
                        enemyShips.append(current_ship)
                elif current_ship.checkSize(randomColumn) and direction == "down":  # same as prior if, but does down instead of right
                    overridesShip = False
                    for k in range(current_ship.getSize()):
                        if not enemyGrid[randomRow][randomColumn + k] == tempEnemyGrid[randomRow][randomColumn + k]:
                            overridesShip = True
                    if not overridesShip:
                        for k in range(current_ship.getSize()):
                            enemyGrid[randomRow][randomColumn + k] = button.Button(50 * randomRow + size[0] / 1.5, 50 * (randomColumn + k) + size[1] / 3, grid_Square, 50,50)  # for loop that changes the image to the current ships image
                            enemyShipStorer[randomRow][randomColumn + k] = shipNum
                    else:
                        enemyShips.append(current_ship)

                else:
                    enemyShips.append(current_ship)  # if the other 2 if statements fail, it reappends the ship to allow the user to retry
                if len(enemyShips) == 0:
                    turn = 1
            if enemyGrid[row][column].draw(screen) and time.get_ticks() - timeSinceSceneChange > 100 and turn == 1:
                isAttackablePlayer = True
                timeSinceSceneChange = time.get_ticks()
                for i in range(len(chosenAttacksPlayer)):
                    if chosenAttacksPlayer[i] == (row,column):
                        isAttackablePlayer = False

                if isAttackablePlayer:
                    chosenAttacksPlayer.append((row,column))

                if enemyGrid[row][column] != tempEnemyGrid[row][column] and isAttackablePlayer:
                    enemyGrid[row][column] = button.Button(50 * row + size[0] / 1.5, 50 * column + size[1] / 3, orange_Circle, 50, 50)
                    enemyShipStorer[row][column] += 10
                    turn = 2
                    counter5L = 0
                    counter4L = 0
                    counter3L = 0
                    counter2L = 0
                    counter2L2 = 0
                    for i in range(10):
                        for j in range(10):
                            if enemyShipStorer[i][j] == 15:
                                counter5L += 1
                            elif enemyShipStorer[i][j] == 14:
                                counter4L += 1
                            elif enemyShipStorer[i][j] == 13:
                                counter3L += 1
                            elif enemyShipStorer[i][j] == 12:
                                counter2L += 1
                            elif enemyShipStorer[i][j] == 11:
                                counter2L2 += 1
                    if counter5L == 5:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 15:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter4L == 4:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 14:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter3L == 3:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 13:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter2L == 2:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 12:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                    if counter2L2 == 2:
                        for i in range(10):
                            for j in range(10):
                                if enemyShipStorer[i][j] == 11:
                                    enemyGrid[i][j] = button.Button(50 * i + size[0] / 1.5, 50 * j + size[1] / 3, black_Square, 50, 50)
                elif enemyGrid[row][column] == tempEnemyGrid[row][column] and isAttackablePlayer:
                    enemyGrid[row][column] = button.Button(50 * row + size[0] / 1.5, 50 * column + size[1] / 3, red_cross, 50, 50)
                    turn = 2
                timeSinceSceneChange = time.get_ticks()
            if turn == 2 and time.get_ticks() - timeSinceSceneChange > 1:
                isAttackable = True
                randomRow = random_integers(0, 9)
                randomColumn = random_integers(0, 9)
                for i in range(len(chosenAttacks)):
                    if chosenAttacks[i] == (randomRow, randomColumn):
                        isAttackable = False
                if not (randomRow + randomColumn) % 2 == 0:
                    isAttackable = False
                if isAttackable:
                    chosenAttacks.append((randomRow, randomColumn))

                if playerGrid[randomRow][randomColumn] != tempPlayerGrid[randomRow][randomColumn] and isAttackable:
                    playerGrid[randomRow][randomColumn] = button.Button(50 * randomRow + size[0] / 5, 50 * randomColumn + size[1] / 3, attacked_Ship , 50,50)
                    turn = 1
                    timeSinceSceneChange = time.get_ticks()
                    playerShipStorer[randomRow][randomColumn] += 10
                    counter5L = 0
                    counter4L = 0
                    counter3L = 0
                    counter2L = 0
                    counter2L2 = 0
                    for i in range(10):
                        for j in range(10):
                            if playerShipStorer[i][j] == 15:
                                counter5L += 1
                            elif playerShipStorer[i][j] == 14:
                                counter4L += 1
                            elif playerShipStorer[i][j] == 13:
                                counter3L += 1
                            elif playerShipStorer[i][j] == 12:
                                counter2L += 1
                            elif playerShipStorer[i][j] == 11:
                                counter2L2 += 1
                    if counter5L == 5:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 15:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                     black_Square, 50, 50)
                    if counter4L == 4:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 14:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                     black_Square, 50, 50)
                    if counter3L == 3:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 13:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                     black_Square, 50, 50)
                    if counter2L == 2:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 12:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                     black_Square, 50, 50)
                    if counter2L2 == 2:
                        for i in range(10):
                            for j in range(10):
                                if playerShipStorer[i][j] == 11:
                                    playerGrid[i][j] = button.Button(50 * i + size[0] / 5, 50 * j + size[1] / 3,
                                                                     black_Square, 50, 50)

                elif playerGrid[randomRow][randomColumn] == tempPlayerGrid[randomRow][randomColumn] and isAttackable:
                    playerGrid[randomRow][randomColumn] = button.Button(50 * randomRow + size[0] / 5, 50 * randomColumn + size[1] / 3, red_cross, 50,50)
                    turn = 1
                    timeSinceSceneChange = time.get_ticks()
        if backButton.draw(screen) and time.get_ticks() - timeSinceSceneChange > 100:
            currentScene = backStack.pop()
            turn = -1
            resetShipLists()
            for row in range(10):
                for column in range(10):
                    playerGrid[row][column] = tempPlayerGrid[row][column]
                    enemyGrid[row][column] = tempEnemyGrid[row][column]
            timeSinceSceneChange = time.get_ticks()

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
        currentScene = statisticsMenuScene(currentScene)

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
