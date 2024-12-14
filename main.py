import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    color = 0, 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color)
        pygame.display.flip()
        
        # limits framerate
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()