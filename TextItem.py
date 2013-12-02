import pygame

class TextItem:

    def __init__(self, x, y, width, height, text, color=(0, 0, 255)):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.setText(text)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (
            self.x, self.y, self.width, self.height), 0)
        screen.blit(self.textObj, self.textRectObj)

    def setText(self, text):
        self.text = text
        self.textObj = self.fontObj.render(text, True, (0, 255, 0))
        self.textRectObj = self.textObj.get_rect()
        self.textRectObj.center = (self.x + (self.width / 2), self.y + (self.height / 2))