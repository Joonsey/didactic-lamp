import pygame
import sys

pygame.init()

WIDTH=1080
HEIGHT=720
CAPTION="Totally not risk of rain"

class Game():
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(CAPTION)


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_q]:
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            self.window.fill((0,0,0))
            self.handle_input()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
