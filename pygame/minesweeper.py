import pygame
import sys

from random import randrange

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (127, 127, 127)

WIDTH = 30
HEIGHT = 30

SQUARES_NUMBER = 10

MARGIN = 5


class Game:
    def __init__(self):
        self.grid = [[self.Cell(x, y) for x in range(SQUARES_NUMBER)] for y in range(SQUARES_NUMBER)]
        self.init = False

        self.num_bombs = 10

        self.squares_x = SQUARES_NUMBER
        self.squares_y = SQUARES_NUMBER

    def draw(self):
        screen.fill(BLACK)

        for row in range(self.squares_y):
            for column in range(self.squares_x):
                color = WHITE
                if self.grid[row][column].is_visible:
                    color = RED if self.grid[row][column].has_bomb else GRAY

                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH, HEIGHT])

                self.grid[row][column].show_text()

    def place_bombs(self, row, column):
        placed_bombs = 0
        while placed_bombs < self.num_bombs:
            x = randrange(self.squares_y)
            y = randrange(self.squares_x)

            if not self.grid[x][y].has_bomb and not (row == x and column == y):
                self.grid[x][y].has_bomb = True
                placed_bombs += 1

        self.count_all_bombs()

        if self.grid[row][column].bomb_count != 0:
            self.place_bombs(row, column)

    def count_all_bombs(self):
        for row in range(self.squares_y):
            for column in range(self.squares_x):
                self.grid[row][column].count_bombs(self.squares_y, self.squares_x)

    def click_handle(self, row, column, button):
        if button == pygame.BUTTON_LEFT:
            if not self.init:
                self.place_bombs(row, column)
                self.init = True

            self.grid[row][column].is_visible = True

    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y

            self.test = False
            self.is_visible = False

            self.has_bomb = False
            self.bomb_count = 0

            self.text = ""

        def show_text(self):
            if self.is_visible:
                if self.bomb_count == 0:
                    self.text = font.render("", True, BLACK)
                else:
                    self.text = font.render(str(self.bomb_count), True, BLACK)

                screen.blit(self.text, (self.x * (WIDTH + MARGIN) + 12, self.y * (HEIGHT + MARGIN) + 10))

        def count_bombs(self, squaresx, squaresy):
            if not self.test:
                self.test = True
                if not self.has_bomb:
                    for column in range(self.x - 1, self.x + 2):
                        for row in range(self.y - 1, self.y + 2):
                            if (0 <= row < squaresx and 0 <= column < squaresy
                                    and not (column == self.x and row == self.y)
                                    and game.grid[row][column].has_bomb):
                                self.bomb_count += 1


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sapper")

    size = (SQUARES_NUMBER * (WIDTH + MARGIN) + MARGIN, (SQUARES_NUMBER * (HEIGHT + MARGIN) + MARGIN))
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    font = pygame.font.Font('freesansbold.ttf', 24)

    game = Game()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()

                column = position[0] // (WIDTH + MARGIN)
                row = (position[1]) // (HEIGHT + MARGIN)

                if row >= game.squares_y:
                    row = game.squares_y - 1

                if column >= game.squares_x:
                    column = game.squares_x - 1

                if row >= 0:
                    game.click_handle(row, column, event.button)

        game.draw()
        clock.tick(60)
        # Update the screen
        pygame.display.flip()
