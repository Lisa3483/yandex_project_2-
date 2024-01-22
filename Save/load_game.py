import pygame
import sqlite3

unic_number = 0
r = True


class Saves:
    def __init__(self, screen, menu):
        pygame.init()
        self.screen = screen
        self.x, self.y = 800, 600
        self.flag = 2
        self.menu = menu
        self.name = ''

    def flagg(self):
        return self.flag

    def get_name(self):
        return self.name

    def all_events(self):
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
        global unic_number, r
        r = True
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

                result = cur.execute("""SELECT name FROM save_game WHERE id = ?""", (i + 1,)).fetchall()
                result.sort()
                res1 = cur.execute("""SELECT unic_number FROM save_game WHERE id = ?""", (i + 1,)).fetchall()
                self.name = result[0][0]
                if result[0][0] != 'Пустой слот':
                    unic_number = res1[0][0]
                    r = False
    def game(self):
        global unic_number
        return unic_number

    def new_game(self):
        self.flag = 7
        return self.flag

    def ff(self):
        global r
        return r

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM save_game").fetchall()
        font = pygame.font.Font(None, 32)

        result.sort()

        c = 0
        for i in result:
            text = font.render(i[1], True, (255, 255, 255))
            self.screen.blit(text, (self.x // 4, 45 + 130 * c))
            c += 1
        con.close()