import pygame
import sqlite3


class Statistics:
    def __init__(self, screen, menu):
        self.x, self.y = 800, 600
        self.screen = screen
        self.menu = menu
        self.running = True
        self.flag = 3

    def all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.buttons()

    def flagg(self):
        return self.flag

    def okno(self):
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        stats = ['Смерти', 'Убито', 'Время', 'Выиграно', 'Сыграно']
        pygame.draw.rect(self.screen, (153, 102, 5), (5, self.y - 65, 110, 40), 0)
        font = pygame.font.Font(None, 28)
        text = font.render('В меню', True, (255, 255, 255))
        text_x = 20
        text_y = self.y - 55
        self.screen.blit(text, (text_x, text_y))

        for j in range(5):
            pygame.draw.rect(self.screen, (153, 102, 5), (3, 5, self.x - 5, 50), 5)

        for j in stats:
            font = pygame.font.Font(None, 28)
            text = font.render(j, True, (255, 255, 255))
            text_x = 65 + (stats.index(j)) * ((self.x - 60) // 5 + 5)
            text_y = 15
            self.screen.blit(text, (text_x, text_y))

        self.baza()
        pygame.display.flip()

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 5 < self.mouse_x < 115 and self.y - 65 < self.mouse_y < self.y - 15:
            self.running = False
            if self.menu == 'start':
                self.flag = 1
            else:
                self.flag = 10

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM stats").fetchall()
        result.sort(reverse=True)
        c = 0
        if len(result) == 0:
            font = pygame.font.Font(None, 38)
            text = font.render('Тут пока ничего нет', True, (255, 255, 255))
            self.screen.blit(text, (200, self.y // 2))

        for i in result[:8]:
            n = 0
            font = pygame.font.Font(None, 28)
            text = font.render(str(i[-1]), True, (255, 255, 255))
            text_x = 20
            text_y = 75 + c
            self.screen.blit(text, (text_x, text_y))
            pygame.draw.line(self.screen, (153, 102, 5), (5, 55), (5, 110 + c), 5)

            for j in i[:-1]:
                text = font.render(str(j), True, (255, 255, 255))
                text_x = 65 + (n * ((self.x - 60) // 5 + 5))
                self.screen.blit(text, (text_x, text_y))
                pygame.draw.line(self.screen, (153, 102, 5), (((self.x - 60) // 5) * n + 55, 5),
                                 (((self.x - 60) // 5) * n + 55, 110 + c), 5)
                n += 1
            pygame.draw.line(self.screen, (153, 102, 5), (self.x - 5, 5), (self.x - 5, 110 + c),
                             5)
            c += 55
            pygame.draw.line(self.screen, (153, 102, 5), (5, (55 + c)), ((self.x - 5), (55 + c)),
                         5)

        con.close()


