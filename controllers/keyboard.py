import pygame

class KeyboardController:
    def get_left_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return -1
        elif keys[pygame.K_s]:
            return 1
        return 0

    def get_right_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return -1
        elif keys[pygame.K_DOWN]:
            return 1
        return 0
