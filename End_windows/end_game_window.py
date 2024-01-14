import pygame
import sqlite3


class EndGame:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.flag = 9
        self.x, self.y = 800, 600
        self.mouse_x, self.mouse_y = 0, 0

    def flagg(self):
        return self.flag

    def all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                self.button()


    def okno(self):
        image = pygame.image.load('images/zakat.png').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        font = pygame.font.SysFont('serif', 54)
        text = font.render('Вы успешно сбежали с острова!', True, 'white')
        w = text.get_rect().width
        self.screen.blit(text, (self.x // 2 - w // 2, 100))
        font = pygame.font.Font(None, 32)
        text = font.render('Результаты:', True, 'white')
        self.screen.blit(text, (50, 200))
        stats = ['Смерти', 'Убито', 'Время', 'Выиграно', 'Сыграно']
        pygame.draw.line(self.screen, 'white', (20, 325), (self.x - 21, 325), 2)
        font = pygame.font.Font(None, 38)
        for i in range(5):
            pygame.draw.rect(self.screen, 'white',
                             (20 + ((self.x - 40) // 5 * i), 250, (self.x - 40) // 5, 150), 2)
            text = font.render(stats[i], True, 'white')
            self.screen.blit(text, (35 + ((self.x - 40) // 5 * i), 275))
        pygame.draw.rect(self.screen, 'white', (self.x // 2 - 100, 450, 200, 70), 5)
        font = pygame.font.Font(None, 48)
        text = font.render('В меню', True, 'white')
        w = text.get_rect().width
        h = text.get_rect().height
        self.screen.blit(text, (self.x // 2 - w // 2, 450 + h // 2))
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM stats WHERE id = ?", (self.game,)).fetchall()
        con.close()
        pygame.display.flip()

    def button(self):
        if self.x // 2 - 100 <= self.mouse_x <= self.x // 2 + 100 and 450 <= self.mouse_y <= 520:
            self.flag = 1
