import pygame

pygame.init()

RESOLUTION = 330, 900
FPS = 60

display = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            if event.key == pygame.K_ESCAPE:
                exit()

    pygame.display.flip()
    clock.tick(FPS)

