from game.pong import PongGame
from controllers.keyboard import KeyboardController

def main():
    controller = KeyboardController()
    game = PongGame(controller)
    game.run()

if __name__ == "__main__":
    main()
