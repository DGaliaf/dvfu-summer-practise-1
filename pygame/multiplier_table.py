import pygame
import math

WIDTH, HEIGHT = 800, 800


def calculate_coordinates(angle, radius, center_x, center_y):
    x = int(math.cos(math.radians(angle)) * radius) + center_x
    y = int(math.sin(math.radians(angle)) * radius) + center_y
    return x, y


def draw_table(screen, multiplier):
    screen.fill((0, 0, 0))
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    radius = 200

    for i in range(1, 361):
        color = pygame.Color(0)
        color.hsva = (i * multiplier % 1, 100, 100, 100)
        x1, y1 = calculate_coordinates(i, radius, center_x, center_y)
        x2, y2 = calculate_coordinates(i * multiplier, radius, center_x, center_y)
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lutaia Narkomania")
    clock = pygame.time.Clock()

    running = True
    animation_running = True
    multiplier = 2

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    animation_running = not animation_running

        if animation_running:
            multiplier += 0.01

        draw_table(screen, multiplier)

        pygame.display.update()

    pygame.quit()
