import pygame
import sqlite3


class SaveGame:
    def __init__(self, screen, name, menu, unic_number):
        self.x, self.y = 800, 600
        self.name = name
        self.menu = menu
        self.unic_number = unic_number
        self.unic_number = unic_number
        self.flag = 12
        self.screen = screen

    def get_unic_number(self):
        return self.unic_number

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
            if self.menu == 'start':
                self.flag = 1
            else:
                self.flag = 10

        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()

        for i in range(4):
            if 5 + i * 130 < self.mouse_y < 130 + i * 130 and 5 < self.mouse_x < self.x - 5:
                if self.unic_number == 0:
                    con = sqlite3.connect('DataBase/stat.db')
                    cur = con.cursor()
                    result = cur.execute("""SELECT * FROM stats""").fetchall()[0]
                    self.id = result[0] + 1
                    self.unic_number = self.id
                    res = """INSERT INTO stats (unic_number, deaths, kills, time, wins, battles) 
                    VALUES (?, 0, 0, 0, 0, 0);"""
                    res1 = (self.id,)
                    cur.execute(res, res1)
                    con.commit()
                    res2 = """INSERT INTO save_game (unic_number, name, id) VALUES (?, ?, ?)"""
                    res1 = (self.id, self.name, i + 1)
                    cur.execute(res2, res1)
                    con.commit()
                    con.close()
                else:

                    res = """INSERT INTO save_game (unic_number, name, id) VALUES (?, ?, ?);"""
                    res1 = (self.unic_number, self.name, i + 1)
                    cur.execute(res, res1)
                    con.commit()
                    self.okno()
                self.flag = 7
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
        con.close()

