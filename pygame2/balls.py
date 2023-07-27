import pygame
import random
import sys



all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites, balls)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        self.check_collision()
        self.check_border_collision()

    def check_collision(self):
        for ball in balls:
            if ball != self:
                distance = pygame.math.Vector2(ball.rect.center).distance_to(self.rect.center)
                sum_radii = self.radius + ball.radius
                if distance < sum_radii:
                    self.vx = -self.vx
                    self.vy = -self.vy

    def check_border_collision(self):
        for border in horizontal_borders.sprites() + vertical_borders.sprites():
            if pygame.sprite.collide_rect(self, border):
                self.vx = -self.vx
                self.vy = -self.vy


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)

        if x1 == x2:  # вертикальная граница
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
            vertical_borders.add(self)
        else:  # горизонтальная граница
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
            horizontal_borders.add(self)


if __name__ == "__main__":
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)

    running = True
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                Ball(20, x - 20, y - 20)

        all_sprites.update()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
