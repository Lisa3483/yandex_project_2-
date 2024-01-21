import pygame
import sqlite3

color = (153, 153, 153)
active = False
text = ''
warning = ''


class Name:
    def __init__(self, screen):
        self.font = pygame.font.Font(None, 32)
        self.flag = 5
        self.x, self.y = 800, 600
        self.screen = screen
        self.rec = pygame.Rect(self.x / 3, 2 * (self.y / 3) - 50, self.x / 3, 50)

    def names(self):
        global text
        return text


    def all_events(self):
        global color, active, text, warning
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.rec.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = (255, 255, 255) if active else (153, 153, 153)

                if self.x // 2 - 80 < mouse_x < self.x // 2 + 80 \
                    and self.y // 2 - 30 < mouse_y < self.y // 2 + 30:
                    self.button()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 10:
                            text += event.unicode
                        else:
                            warning = 'Максимальное количество символов - 10'
            pygame.display.flip()

    def okno(self):
        global warning
        global color, text
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        font = pygame.font.Font(None, 33)
        text_1 = font.render('Введите имя вашего персонажа', True, (255, 255, 255))
        self.screen.blit(text_1, (220, 200))
        pygame.draw.rect(self.screen, (153, 102, 5),
                         (self.x / 4, self.y / 4, self.x // 2, self.y // 2), 5)
        pygame.draw.rect(self.screen, color, self.rec, 0)
        pygame.draw.rect(self.screen, (153, 102, 5), (self.x // 2 - 80, self.y // 2 - 30, 160, 60))
        text_1 = font.render('Подтвердить', True, (255, 255, 255))
        self.screen.blit(text_1, (self.x // 2 - 75, self.y // 2 - 15))

        txt = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(txt, (self.rec.x + 5, self.rec.y + 5))

        font_0 = pygame.font.Font(None, 20)
        text_0 = font_0.render(warning, True, (255, 0, 0))
        self.screen.blit(text_0, (270, 2 * (self.y / 3) + 20))

    def button(self):
        global text, warning
        if len(text) < 5:
            warning = 'Минимальное количество символов - 5'

        else:
            self.flag = 12

    def flagg(self):
        return self.flag



