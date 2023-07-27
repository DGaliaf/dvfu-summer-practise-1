import pygame


if __name__ == "__main__":
    WIDTH, N = 400, 10

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Chessboard')

    # Рисование шахматной доски
    cell_size = WIDTH // N
    colors = [(0, 0, 0), (255, 255, 255)]

    for row in range(N):
        for col in range(N):
            color_index = (row + col) % 2
            pygame.draw.rect(screen, colors[color_index], (col * cell_size, row * cell_size, cell_size, cell_size))
    # --------------------------------

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
