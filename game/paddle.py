import pygame

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 5

    def move(self, direction):
        self.rect.y += direction * self.speed
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
