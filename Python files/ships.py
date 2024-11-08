import pygame

class Ship():
    def __init__(self, size, image, givenRotation):
        self.size = size
        self.image = image
        self.rotation = givenRotation
        self.xPos = 0
        self.yPos = 0

    def getImage(self):
        return self.image

    def getSize(self):
        return self.size

    def getRotation(self):
        return self.rotation

    def setPos(self, givenX, givenY):
        self.xPos = givenX
        self.yPos = givenY

    def setRotation(self, givenRotation):
        self.rotation = givenRotation

    def checkSize(self, i):
        if 10 - self.size > i:
            return True
        return False