import pygame, time, random
pygame.init()


w, h = 700, 600
screen = pygame.display.set_mode((w, h))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sprite = pygame.image.load("spaceship.png")
        pygame.transform.scale(self.sprite, (1, 1))
        self.rect = self.sprite.get_rect()
        self.rect.move_ip(10, 500)

    def draw(self):
        pass

    def collision(self):
        pass


player = Player()

while True: # Main GameLoop
    # EventLoop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))
    screen.blit(player.sprite, player.rect)
    player.draw()
