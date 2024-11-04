import pygame

class Button():
    #instantiates buttons
    def __init__(self,xCoord,yCoord, imageGiven , givenScale):
        imageGiven = pygame.transform.scale(imageGiven, (givenScale*3, givenScale)) #makes image the size of the givenScale in a 3:1 ratio of x:y
        self.image = imageGiven
        self.rect = self.image.get_rect()
        self.rect.topleft = (xCoord, yCoord)
        self.clicked = False


    #draws buttons and creates collision detection
    def draw(self, surface):
        clicked = False

        #gets mouse position
        pos = pygame.mouse.get_pos()

        #checks if mouse is hovering over and clicking
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return clicked