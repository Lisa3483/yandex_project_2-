import pygame
import sqlite3


flag = True


class StartStateMenu:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = 800, 600

        pygame.init()
        pygame.display.set_caption('The little world')

        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        screen.blit(new_image, (0, 0))

        for i in range(4):
            pygame.draw.rect(self.screen, (0, 150, 0), (250, 230 + i * 70, 300, 50), 0)

        pygame.draw.rect(self.screen, (0, 150, 0), (230, 140, 340, 70), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (200, 10, 400, 120), 5)

        self.text_button()

        pygame.display.flip()

    def text_button(self):
        words = ["Загрузить игру", "Сохранения", "Статистика", "Выход"]

        font = pygame.font.Font(None, 28)

        for i in words:
            text = font.render(i, True, (255, 255, 255))
            text_y = 245 + words.index(i) * 70
            self.screen.blit(text, (260, text_y))

        font = pygame.font.Font(None, 35)
        text = font.render("Начало новой игры", True, (255, 255, 255))
        text_x = 260
        text_y1 = 165
        self.screen.blit(text, (text_x, text_y1))

        font = pygame.font.SysFont('serif', 60)
        text = font.render("The little world", True, (255, 255, 255))
        text_x0 = 215
        text_y = 50
        self.screen.blit(text, (text_x0, text_y))


class Buttons:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = 800, 600
        self.click_buttons()

        pygame.display.flip()

    def click_buttons(self):
        global flag
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if 250 <= mouse_x <= 550:
            if 220 <= mouse_y <= 270:
                self.screen.fill('white')
                flag = False

            elif 290 <= mouse_y <= 340:
                flag = False
                Saves()

            elif 360 <= mouse_y <= 410:
                flag = False
                Statistic()

            elif 430 <= mouse_y <= 480:
                flag = False
                Exit()

            if 230 <= mouse_x <= 570 and 140 <= mouse_y <= 210:
                flag = False
                Name()

class Name:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 32)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        self.x, self.y = 800, 600
        self.screen = screen
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        self.running = True
        self.color = (0, 150, 0)
        self.rec = pygame.Rect(self.x / 3, 2 * (self.y / 3) - 50, self.x / 3, 50)
        active = False
        self.text = ''

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                    if self.rec.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    self.color = (0, 255, 0) if active else (0, 150, 0)
                    if self.x // 2 - 80 < self.mouse_x < self.x // 2 + 80 \
                        and self.y // 2 - 30 < self.mouse_y < self.y // 2 + 30:
                        self.button()
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            if len(self.text) < 10:
                                self.text += event.unicode
                            else:
                                image = pygame.image.load('images/sstone.jpeg').convert_alpha()
                                new_image = pygame.transform.scale(image, (self.x, self.y))
                                self.screen.blit(new_image, (0, 0))
                                self.scr()
                                font_0 = pygame.font.Font(None, 20)
                                text_0 = font_0.render('Максимальное количество символов - 10', True, (255, 0, 0))
                                self.screen.blit(text_0, (270, 2 * (self.y / 3) + 20))

            self.scr()
            pygame.display.flip()

    def scr(self):
        font = pygame.font.Font(None, 33)
        text = font.render('Введите имя вашего персонажа', True, (255, 255, 255))
        self.screen.blit(text, (220, 200))
        pygame.draw.rect(self.screen, (0, 150, 0),
                         (self.x / 4, self.y / 4, self.x // 2, self.y // 2), 5)
        pygame.draw.rect(self.screen, self.color, self.rec, 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (self.x // 2 - 80, self.y // 2 - 30, 160, 60))
        text = font.render('Подтвердить', True, (255, 255, 255))
        self.screen.blit(text, (self.x // 2 - 75, self.y // 2 - 15))

        txt = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(txt, (self.rec.x + 5, self.rec.y + 5))

    def button(self):
        if len(self.text) < 5:
            image = pygame.image.load('images/sstone.jpeg').convert_alpha()
            new_image = pygame.transform.scale(image, (self.x, self.y))
            self.screen.blit(new_image, (0, 0))
            self.scr()
            font_0 = pygame.font.Font(None, 20)
            text_0 = font_0.render('Минимальное количество символов - 5', True, (255, 0, 0))
            self.screen.blit(text_0, (270, 2 * (self.y / 3) + 20))

        else:
            self.running = False
            SaveGame(self.text)

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM save_game").fetchall()
        font = pygame.font.Font(None, 32)

        c = 0
        for i in result:
            text = font.render(i[1], True, (255, 255, 255))
            self.screen.blit(text, (self.x // 4, 45 + 105 * c))
            c += 1

class SaveGame:
    def __init__(self, name):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.x, self.y = 800, 600
        self.name = name

        self.scr()
        self.running = True

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons()

    def scr(self):
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))

        pygame.draw.rect(self.screen, (0, 150, 0), (5, self.y - 65, 110, 40), 0)
        font = pygame.font.Font(None, 28)
        text = font.render('В меню', True, (255, 255, 255))
        text_x = 20
        text_y = self.y - 55
        self.screen.blit(text, (text_x, text_y))
        for i in range(4):
            pygame.draw.rect(self.screen, (0, 150, 0), (5, 5 + 130 * i, self.x - 10, 125), 5)

        self.baza()

    def buttons(self):
        print(1)
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        for i in range(4):
            if 5 + i * 130 < self.mouse_y < 130 + i * 130 and 5 < self.mouse_x < self.x - 5:
                res = """INSERT INTO save_game (id, name) VALUES (?, ?);"""
                res1 = (i + 1, self.name)
                cur.execute(res, res1)
                con.commit()
                cur.close()
                self.scr()

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM save_game").fetchall()
        font = pygame.font.Font(None, 32)

        c = 0
        for i in result:
            for j in range(4):
                if i[0] == j + 1:
                    text = font.render(i[1], True, (255, 255, 255))
                    self.screen.blit(text, (self.x // 4, 45 + 130 * c))
                    c += 1
        cur.close()

class Saves:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.x, self.y = 800, 600

        self.scr()
        self.running = True

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons()

    def scr(self):
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))

        pygame.draw.rect(self.screen, (0, 150, 0), (5, self.y - 65, 110, 40), 0)
        font = pygame.font.Font(None, 28)
        text = font.render('В меню', True, (255, 255, 255))
        text_x = 20
        text_y = self.y - 55
        self.screen.blit(text, (text_x, text_y))
        for i in range(4):
            pygame.draw.rect(self.screen, (0, 150, 0), (5, 5 + 130 * i, self.x - 10, 125), 5)

        self.baza()

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 5 < self.mouse_x < 115 and self.y - 65 < self.mouse_y < self.y - 15:
            self.running = False
            Main()

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


class Statistic:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.x, self.y = 800, 600
        self.screen = screen
        self.scr()
        self.running = True
        self.baza()

        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons()
    def scr(self):
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))
        stats = ['Общее время', 'Смерти', 'Сыграно', 'Выиграно', 'Убито']
        pygame.draw.rect(self.screen, (0, 150, 0), (5, self.y - 65, 110, 40), 0)
        font = pygame.font.Font(None, 28)
        text = font.render('В меню', True, (255, 255, 255))
        text_x = 20
        text_y = self.y - 55
        self.screen.blit(text, (text_x, text_y))

        for j in range(5):
            pygame.draw.rect(self.screen, (0, 150, 0), (3, 5, self.x - 5, 50), 5)

        for j in stats:
            font = pygame.font.Font(None, 28)
            text = font.render(j, True, (255, 255, 255))
            text_x = 65 + (stats.index(j)) * ((self.x - 60) // 5 + 5)
            text_y = 15
            self.screen.blit(text, (text_x, text_y))

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 5 < self.mouse_x < 115 and self.y - 65 < self.mouse_y < self.y - 15:
            self.running = False
            Main()

    def baza(self):
        con = sqlite3.connect('DataBase/stat.db')
        cur = con.cursor()
        result = cur.execute("SELECT * FROM stats").fetchall()
        c = 0

        for i in result[:8]:
            n = 0
            font = pygame.font.Font(None, 28)
            text = font.render(str(i[-1]), True, (255, 255, 255))
            text_x = 20
            text_y = 75 + c
            self.screen.blit(text, (text_x, text_y))
            pygame.draw.line(self.screen, (0, 150, 0), (5, 55), (5, 110 + c), 5)

            for j in i[:-1]:
                text = font.render(str(j), True, (255, 255, 255))
                text_x = 65 + (n * ((self.x - 60) // 5 + 5))
                self.screen.blit(text, (text_x, text_y))
                pygame.draw.line(self.screen, (0, 150, 0), (((self.x - 60) // 5) * n + 55, 5),
                                 (((self.x - 60) // 5) * n + 55, 110 + c), 5)
                n += 1
            pygame.draw.line(self.screen, (0, 150, 0), (self.x - 5, 5), (self.x - 5, 110 + c), 5)
            c += 55
            pygame.draw.line(self.screen, (0, 150, 0), (5, (55 + c)), ((self.x - 5), (55 + c)),
                         5)

        con.close()


class Exit:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.x, self.y = 800, 600
        self.screen = screen
        self.exxit()
        self.running = True


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons()

    def exxit(self):

        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))

        pygame.draw.rect(self.screen, (0, 150, 0), (100, 100, 600, 400), 5)

        font = pygame.font.Font(None, 40)
        text = font.render("Вы точно хотите выйти?", True, (255, 255, 255))
        self.screen.blit(text, (240, 140))

        pygame.draw.rect(self.screen, (0, 150, 0), (160, 350, 200, 50), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (440, 350, 200, 50), 0)

        font = pygame.font.Font(None, 40)

        text = font.render("ДА", True, (255, 255, 255))
        self.screen.blit(text, (230, 360))

        text = font.render("НЕТ", True, (255, 255, 255))
        self.screen.blit(text, (510, 360))
        pygame.display.flip()

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 160 <= self.mouse_x <= 360 and 350 <= self.mouse_y <= 400:
            pygame.quit()
            exit()

        elif 440 <= self.mouse_x <= 640 and 350 <= self.mouse_y <= 400:
            self.running = False
            Main()


class Main:
    def __init__(self):
        global flag
        flag = True
        screen = pygame.display.set_mode((800, 600))
        StartStateMenu(screen)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Buttons(screen)
                    if flag is False:
                        running = False









