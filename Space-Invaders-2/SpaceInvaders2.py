import pygame
pygame.init()


w, h = 700, 600
screen = pygame.display.set_mode((w, h))

FPS = 25
SHOOT_COOLDOWN = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.body = pygame.Surface((40, 20))
        self.gun = pygame.Surface((10, 20))
        self.body.fill((0, 255, 0))
        self.gun.fill((0, 255, 0))
        self.rect = self.body.get_rect()
        self.rect.move_ip(10, 500)

        self.shoot = None

        self.bullet = pygame.Surface((10, 20))
        self.bullet.fill((255, 0, 0))
        self.bullet_rect = self.bullet.get_rect()
        self.bullet_rect.move_ip(self.rect.x + self.rect.w // 2.52, self.rect.y - 15)
        self.distance = self.bullet_rect.y

    def draw(self):
        screen.blit(self.bullet, self.bullet_rect)
        screen.blit(self.body, self.rect)
        screen.blit(self.gun, (self.rect.x + self.rect.w // 2.52, self.rect.y - 15))

    def movement(self):
        # Player Movement
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 8
        if keys[pygame.K_RIGHT] and self.rect.x <= screen.get_width() - self.rect.w:
            self.rect.x += 8
        # Bullet Movement
        if keys[pygame.K_UP]:
            self.shoot = True

        if self.shoot:
            self.bullet_rect.y -= 20
        else:
            self.bullet_rect.x = self.rect.x + self.rect.w // 2.52
            self.bullet_rect.y = self.rect.y - 15

        if self.bullet_rect.y <= 0:
            self.shoot = False

        if self.rect.x:
            self.rect.move(0, self.rect.y)

    def collision(self):
        pass

class Enemy(pygame.sprite.Sprite):
    pass

player = Player()
enemy = Enemy()

clock = pygame.time.Clock()

while True: # Main GameLoop
    # EventLoop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    player.draw()
    player.movement()
    pygame.display.update()
    clock.tick(FPS)
