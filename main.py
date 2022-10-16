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

    def draw(self):
        self.window.fill((20,12,14))
        pygame.display.update()

    def handle_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_q]:
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            self.handle_input()
            self.handle_quit()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
"""very cool string"""
