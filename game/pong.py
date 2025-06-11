import pygame
from game.paddle import Paddle
from game.ball import Ball

class PongGame:
    def __init__(self, controller):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pong with Pico W")
        self.clock = pygame.time.Clock()
        self.controller = controller

        self.left_paddle = Paddle(30, 250)
        self.right_paddle = Paddle(760, 250)
        self.ball = Ball()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            lp_move = self.controller.get_left_input()
            rp_move = self.controller.get_right_input()

            self.left_paddle.move(lp_move)
            self.right_paddle.move(rp_move)
            self.ball.update(self.left_paddle, self.right_paddle)

            self.screen.fill((0, 0, 0))
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            self.ball.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
