import pygame, sys
pygame.init()

# screen
screen = pygame.display.set_mode((500,700))
clock = pygame.time.Clock()

# game loop
while True:

    for event in pygame.event.get():
        # close screen upon 'x'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update screen 60fps
    pygame.display.update()
    clock.tick(60)
