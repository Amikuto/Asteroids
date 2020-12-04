import pygame
import random

WIDTH = 800
HEIGHT = 1000
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ASTEROIDS!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill("pink")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.key = 'up'

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.key = 'left'
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.key = 'right'
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.key = 'up'
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.key = 'down'
            self.speedy = 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.key)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill("blue")
        self.rect = self.image.get_rect()

        if key == "up":
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedx = 0
            self.speedy = -20

        elif key == "down":
            self.rect.bottom = y + 70
            self.rect.centerx = x
            self.speedx = 0
            self.speedy = 20

        if key == "left":
            self.rect.bottom = y + 20
            self.rect.centerx = x - 40
            self.speedx = -20
            self.speedy = 0

        if key == "right":
            self.rect.bottom = y + 20
            self.rect.centerx = x + 40
            self.speedx = 20
            self.speedy = 0

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left < 0 or self.rect.right > WIDTH:
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((random.randrange(20, 50), random.randrange(20, 50)))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.choice([HEIGHT + 10, -10])
        if self.rect.y == HEIGHT + 10:
            self.speedy = random.randrange(-8, -1)
        elif self.rect.y == -10:
            self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < 0 or self.rect.right > WIDTH or self.rect.bottom < -10:
            self.rect.x = random.randrange(WIDTH)
            self.rect.y = random.choice([HEIGHT + 10, -10])
            if self.rect.y == HEIGHT + 10:
                self.speedy = random.randrange(-8, -1)
            elif self.rect.y == -10:
                self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-5, 5)


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
c = 1
for i in range(c):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Обновление
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False


    # Рендеринг
    screen.fill("black")
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
