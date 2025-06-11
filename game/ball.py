import pygame
import random

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(395, 295, 10, 10)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = random.choice([-4, 4])

    def update(self, left_paddle, right_paddle):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(right_paddle.rect):
            self.speed_x *= -1

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.rect.center = (400, 300)
            self.speed_x *= -1
            self.speed_y = random.choice([-4, 4])

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
