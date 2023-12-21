import pygame


class Thebattlefield:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size,
                    self.cell_size), 1)

        # отрисовка клеточек на клеточном поле
        pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                         (0, 0, self.width * self.cell_size + (2 * self.left), self.top))
        pygame.draw.rect(screen, pygame.Color(202, 196, 176), (
            0, self.height * self.cell_size + self.top, self.width * self.cell_size + (2 * self.left),
            self.height * self.cell_size + (self.top * 2)))
        pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                         (0, 0, self.left, self.height * self.cell_size + self.top * 2))
        pygame.draw.rect(screen, pygame.Color(202, 196, 176),
                         (self.width * self.cell_size + (1 * self.left), 0, self.left,
                          self.height * self.cell_size + self.top * 2))
        # отрисовка рамок для клеточного поля


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Сражение')
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    board = Thebattlefield(16, 8)
    board.set_view(160, 140, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
