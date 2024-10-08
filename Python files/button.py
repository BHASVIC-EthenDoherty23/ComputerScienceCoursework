import pygame

class Button():
    #instantiates buttons
    def __init__(self,xCoord,yCoord, imageGiven):
        self.image = imageGiven
        self.rect = self.image.get_rect()
        self.rect.topleft = (xCoord, yCoord)
        self.clicked = False

    #draws buttons and creates collision detection
    def draw(self, surface):
        action = False

        #gets mouse position
        pos = pygame.mouse.get_pos()

        #checks if mouse is hovering over and clicking
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action