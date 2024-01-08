import pygame
import sqlite3


class Saves:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.x, self.y = 800, 600

        self.running = True

    def flagg(self):
        return self.flag

    def all_events(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons()

    def okno(self):
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))

        pygame.draw.rect(self.screen, (153, 102, 5), (5, self.y - 65, 110, 40), 0)
        font = pygame.font.Font(None, 28)
        text = font.render('В меню', True, (255, 255, 255))
        text_x = 20
        text_y = self.y - 55
        self.screen.blit(text, (text_x, text_y))
        for i in range(4):
            pygame.draw.rect(self.screen, (153, 102, 5), (5, 5 + 130 * i, self.x - 10, 125), 5)

        self.baza()
        pygame.display.flip()

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 5 < self.mouse_x < 115 and self.y - 65 < self.mouse_y < self.y - 15:
            self.running = False
            self.flag = 1

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM save_game").fetchall()
        font = pygame.font.Font(None, 32)

        c = 0
        for i in result:
            text = font.render(i[1], True, (255, 255, 255))
            self.screen.blit(text, (self.x // 4, 45 + 130 * c))
            c += 1
        cur.close()

