import pygame

# Константы для окна
WIDTH, HEIGHT = 400, 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RECTANGLE_COLOR = (255, 0, 0)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ctrl+Z")
    clock = pygame.time.Clock()

    rectangles = []

    drawing = False
    start_pos = None

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and event.mod & pygame.KMOD_CTRL:
                    # Если нажата Ctrl+Z удаляем последний прямоугольник
                    if rectangles:
                        rectangles.pop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    drawing = True
                    start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    drawing = False

                    if start_pos:
                        end_pos = event.pos
                        x = min(start_pos[0], end_pos[0])
                        y = min(start_pos[1], end_pos[1])
                        width = abs(end_pos[0] - start_pos[0])
                        height = abs(end_pos[1] - start_pos[1])
                        rectangles.append([x, y, width, height])
                        start_pos = None

        screen.fill(WHITE)

        for rect in rectangles:
            pygame.draw.rect(screen, RECTANGLE_COLOR, rect, 2)

        pygame.display.update()

    pygame.quit()
