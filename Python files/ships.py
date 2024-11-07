import pygame

class Ship():
    def __init__(self, size, image, givenRotation):
        self.size = size
        self.image = image
        self.rotation = givenRotation
        self.xPos = 0
        self.yPos = 0

    def placeShip(self, grid):
        if self.rotation == "Right":
            for i in range(self.size):
                grid[i + self.xPos][self.yPos]
        if self.rotation == "Down":
            for i in range(self.size):
                grid[self.yPos][i + self.yPos]
        return grid


    def setPos(self, givenX, givenY):
        self.xPos = givenX
        self.yPos = givenY

    def setRotation(self, givenRotation):
        self.rotation = givenRotation