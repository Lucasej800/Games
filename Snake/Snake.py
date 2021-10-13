import pygame
import random
pygame.init()

SPEED = 7

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.direction = "right"
        self.size = 10
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((255, 255, 255))
        self.snake = [100, 50]
        self.body = [
            [90, 50],
            self.snake,
        ]

    def control(self):
        self.body.append(list(self.snake))
        s.fill((0, 0, 0))
        for pos in self.body:
            self.rect = pygame.draw.rect(s, (255, 255, 255), pygame.Rect(
                pos[0], pos[1], 10, 10))
            s.blit(self.surf, self.rect)
        if self.direction == "up":
            self.snake[1] -= 10
        elif self.direction == "down":
            self.snake[1] += 10
        elif self.direction == "left":
            self.snake[0] -= 10
        elif self.direction == "right":
            self.snake[0] += 10


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 0, 50))
        self.rect = self.surf.get_rect()
        self.pos = [random.randrange(1, (w // 10)) * 10,
                    random.randrange(1, (h // 10)) * 10]
        self.rect.move_ip(self.pos)


w = 400
h = 400
s = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

player = Block()
food = Food()

spawn_food = True
cheat = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                cheat = True
            if event.key == pygame.K_UP and player.direction != "down":
                player.direction = "up"
            elif event.key == pygame.K_DOWN and player.direction != "up":
                player.direction = "down"
            elif event.key == pygame.K_RIGHT and player.direction != "left":
                player.direction = "right"
            elif event.key == pygame.K_LEFT and player.direction != "right":
                player.direction = "left"
    clock.tick(SPEED)
    if spawn_food:
        food.pos = [random.randrange(1, (w // 10)) * 10,
                    random.randrange(1, (h // 10)) * 10]
        food.rect.move_ip(-food.pos[0], -food.pos[1])
        food.rect.move_ip(food.pos)
        spawn_food = False
    s.blit(food.surf, food.rect)
    if player.snake[0] == food.pos[0] and player.snake[1] == food.pos[1] or cheat:
        spawn_food = True
        cheat = False
        SPEED += 0.25
    else:
        player.body.pop(0)


    player.control()
    s.blit(food.surf, food.pos)

    if player.snake[0] + 10 <= 0 or player.snake[0] >= w:
        running = False
    if player.snake[1] + 10 <= 0 or player.snake[1] >= h:
        running = False
    for square in player.body[1:]:
        if pygame.Rect(square[0], square[1], 10, 10).colliderect(pygame.Rect(player.snake[0], player.snake[1], 10, 10)):
            running = False

    pygame.display.update()
pygame.quit()
quit()
