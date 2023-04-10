import pygame, sys
pygame.init()

# screen
screen = pygame.display.set_mode((500,700))
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=(250,600))
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.centerx >= 25:
            self.rect.centerx -= 5
        elif keys[pygame.K_RIGHT] and self.rect.centerx <= 475:
            self.rect.centerx += 5
        elif keys[pygame.K_UP] and self.rect.centery >= 25:
            self.rect.centery -= 5
        elif keys[pygame.K_DOWN] and self.rect.centery <= 675:
            self.rect.centery += 5
    def update(self):
        self.movement()
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

# game loop
while True:

    for event in pygame.event.get():
        # close screen upon 'x'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    player_group.draw(screen)

    # update screen 60fps
    player_group.update()
    pygame.display.update()
    clock.tick(60)
