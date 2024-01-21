import pygame


class Death:
    def __init__(self, screen):
        self.screen = screen
        self.flag = 8
        self.x, self.y = 800, 600

    def flagg(self):
        return self.flag

    def all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.buttons(mouse_x, mouse_y)

    def buttons(self, mouse_x, mouse_y):
        if self.x // 6 <= mouse_x <= self.x // 6 + 200 and 450 <= mouse_y <= 500:
            pass

        elif self.x - self.x // 6 - 200 <= mouse_x <= self.x - self.x // 6 and 450 <= mouse_y <= 500:
            self.flag = 1

    def okno(self):
        image = pygame.image.load('images/black_phone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        font = pygame.font.SysFont('serif', 64)
        text = font.render('GAME OVER', True, 'red')
        w = text.get_rect().width
        h = text.get_rect().height
        self.screen.blit(text, (self.x // 2 - w // 2, self.y // 2 - h // 2))
        pygame.draw.rect(self.screen, 'red', (self.x // 6, 450, 200, 50), 5)
        pygame.draw.rect(self.screen, 'red', (self.x - self.x // 6 - 200, 450, 200, 50), 5)
        font = pygame.font.Font(None, 32)
        text = font.render('Загрузить игру', True, 'white')
        w = text.get_rect().width
        h = text.get_rect().height
        self.screen.blit(text, (self.x // 6 + 100 - w // 2, 475 - h // 2))
        text = font.render('В меню', True, 'white')
        w = text.get_rect().width
        h = text.get_rect().height
        self.screen.blit(text, (self.x - self.x // 6 - 100 - w // 2, 475 - h // 2))

        pygame.display.flip()

