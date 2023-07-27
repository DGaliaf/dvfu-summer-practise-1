import pygame


if __name__ == "__main__":
    pygame.init()

    WIDTH, HEIGHT = 300, 300

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Rectangle move')

    SQUARE_SIZE = 50
    square_x, square_y = 50, 50

    offset_x, offset_y = 5, 5

    dragging = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    # Проверка, находится ли курсор внутри квадрата
                    if square_x <= event.pos[0] <= square_x + SQUARE_SIZE and square_y <= event.pos[1] <= square_y + SQUARE_SIZE:
                        dragging = True

                        offset_x = event.pos[0] - square_x
                        offset_y = event.pos[1] - square_y

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    dragging = False

            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    # Перемещение квадрата при перетаскивании
                    square_x = event.pos[0] - offset_x
                    square_y = event.pos[1] - offset_y

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

        pygame.display.update()
