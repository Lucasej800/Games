import pygame
pygame.init()

w, h = (650, 650)
s = pygame.display.set_mode((w, h))
pygame.display.set_caption("Space-Invaders")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

times = 0
move_right = True
move_left = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sprite = pygame.image.load("spaceship.png")
        pygame.transform.scale(self.sprite, (1, 1))
        self.rect = self.sprite.get_rect()
        print(times)

        self.rect.move_ip(10, 500)

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rect.move_ip(50, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.move_ip(-50, 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.rect.move_ip(0, -50)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.rect.move_ip(0, 50)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.sprite = pygame.image.load("enemy.png")
        pygame.transform.scale(self.sprite, (10, 10))
        self.rect = self.sprite.get_rect()
        self.line_1 = [
            [10, 10]
        ]
        self.y = 10

        for i in range(18):
            self.line_1.append([self.line_1[-1][0] + 25, 10])

    ''' 
        self.line_1.append((10, 10))
        self.line_1.append((35, 10))
        self.line_1.append((60, 10))
        self.line_1.append((85, 10))
        self.line_1.append((110, 10))
        self.line_1.append((135, 10))
        self.line_1.append((160, 10))
        self.line_1.append((185, 10))
        self.line_1.append((210, 10))
        self.line_1.append((235, 10))
        self.line_1.append((260, 10))
        self.line_1.append((285, 10))
        self.line_1.append((310, 10))
        self.line_1.append((335, 10))
        self.line_1.append((360, 10))
        self.line_1.append((385, 10))
        self.line_1.append((410, 10))
        self.line_1.append((435, 10))
        self.line_1.append([460, 10])'''

    def spawn(self):
        for i in range(len(self.line_1)):
            if not i % 2:
                s.blit(self.sprite, (self.line_1[i][0], self.line_1[i][1]))
        for i in range(len(self.line_1)):
            if not i % 2:
                s.blit(self.sprite, (self.line_1[i][0], self.line_1[i][1] + 25))
        for i in range(len(self.line_1)):
            if not i % 2:
                s.blit(self.sprite, (self.line_1[i][0], self.line_1[i][1] + 50))
        for i in range(len(self.line_1)):
            if not i % 2:
                s.blit(self.sprite, (self.line_1[i][0], self.line_1[i][1] + 75))

    def right_move(self):
        if move_right:
            if times == 10 or times == 20 or times == 30 or times == 40 or times == 50 or times == 60 and move_right:
                self.line_1.pop(0)
                self.line_1.append([self.line_1[-1][0] + 25, self.line_1[-1][1]])
                print(self.line_1[-1][0])

            if times == 70:
                for i in self.line_1:
                    i[1] += 12.5
            if times == 80:
                for i in self.line_1:
                    i[1] += 12.5
    def left_move(self):
        if move_left:
            if times == 10 or times == 20 or times == 30 or times == 40 or times == 50 or times == 60 and move_left:
                self.line_1.pop(-1)
                self.line_1.insert(0, [self.line_1[0][0] - 25, self.line_1[0][1]])
                print(self.line_1[-1][0])
            if times == 70:
                for i in self.line_1:
                    i[1] += 12.5

            if times == 80:
                for i in self.line_1:
                    i[1] += 12.5


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((5, 10))
        self.surf.fill((0, 200, 0))
        self.rect = self.surf.get_rect()

    def collision(self):
        for i in enemy.line_1:
            if self.rect.x == i[0] and self.rect.y == i[1]:
                i.pop()


s_rect = s.get_rect()

center_x = s_rect.centerx
center_y = s_rect.centery

player = Player()
enemy = Enemy()
bullet = Bullet()
allSprites = pygame.sprite.Group()
allSprites.add(enemy, player, bullet)

enemies = pygame.sprite.Group()
enemies.add(enemy)

enemy.rect.y = 0

c = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            quit()
    if times == 81:
        if move_right:
            move_right = False
            move_left = True
        elif move_left:
            move_right = True
            move_left = False
        times = 0

    c.tick(5)
    times += 1

    allSprites.update()
    if pygame.sprite.spritecollide(bullet, enemies, False):
        print("collide")

    s.fill((0, 0, 0))
    s.blit(player.sprite, player.rect)
    enemy.spawn()
    enemy.right_move()
    enemy.left_move()
    player.move()
    pygame.display.flip()
