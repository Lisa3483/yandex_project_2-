import pygame
import sqlite3
import shelve

flag = 7

class SaveGame:
    def __init__(self, screen, name):
        self.x, self.y = 800, 600
        self.name = name
        self.screen = screen

        self.running = True

    def all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.buttons(mouse_x, mouse_y)

    def flagg(self):
        global flag
        return flag


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

    def buttons(self, mouse_x, mouse_y):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()

        for i in range(4):
            if 5 + i * 130 < mouse_y < 130 + i * 130 and 5 < mouse_x < self.x - 5:
                res = """INSERT INTO save_game (id, name) VALUES (?, ?);"""
                res1 = (i + 1, self.name)
                cur.execute(res, res1)
                con.commit()
                self.okno()
        con.close()

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM save_game").fetchall()
        font = pygame.font.Font(None, 32)

        result.sort()

        c = 0
        for i in result:
            for j in range(4):
                if i[0] == j + 1:
                    text = font.render(i[1], True, (255, 255, 255))
                    self.screen.blit(text, (self.x // 4, 45 + 130 * c))
                    c += 1
        cur.close()

