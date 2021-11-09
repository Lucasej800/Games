import pygame
pygame.init()


w, h = 690, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Space Invaders")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.location_y = 0
        self.image = pygame.image.load("enemy3.png")
        self.rect = self.image.get_rect()
        self.enemy_line1 = [
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
        ]
        self.enemy_line2 = [
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
            self.rect,
        ]

        self.time = 0
        self.speed = 5
        self.amount = len(self.enemy_line1) + len(self.enemy_line2)
        self.living = []

        self.xposition = 0
        self.yposition = 0
        self.xpos = []
        self.ypos = []

        for i in range(self.amount):
            self.xpos.append(self.xposition)
            self.xposition += 50
            self.ypos.append(self.yposition)
            self.living.append(True)


    def draw(self):
        for i in range(self.amount // 2):
            self.enemy_line1[i].x = self.xpos[i]
            self.enemy_line1[i].y = self.ypos[i]
            if self.enemy_line1[i].colliderect(player.bullet_rect):
                if self.living[i]:
                    player.shoot = False
                    print("dead")

            if not self.enemy_line1[i].colliderect(player.bullet_rect):
                if self.living[i]:
                    screen.blit(self.image, self.enemy_line1[i])
            else:
                self.living[i] = False

    def move(self):
        if self.time == 25 or self.time == 50 or self.time == 75 or self.time == 100:
            for i in range(len(self.xpos)):
                self.xpos[i] += 25
        if self.time == 125:
            for i in range(self.amount):
                self.ypos[i] += 50
        if self.time == 150 or self.time == 175 or self.time == 200 or self.time == 225:
            for i in range(len(self.xpos)):
                self.xpos[i] -= 25
        if self.time == 250:
            for i in range(self.amount):
                self.ypos[i] += 25
        if self.time == 250:
            self.time = 0
            self.speed += 1


player = Player()
enemy = Enemy()

clock = pygame.time.Clock()

while True:  # Main GameLoop
    # EventLoop
    enemy.time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    player.draw()
    player.movement()
    enemy.draw()
    enemy.move()
    pygame.display.update()
    clock.tick(FPS)
