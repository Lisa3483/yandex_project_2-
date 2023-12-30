import pygame
import sqlite3
import pickle

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
                pass

class Saves:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        self.x, self.y = 800, 600
        self.screen = screen
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
        for i in range(5):
            pygame.draw.rect(self.screen, (0, 150, 0), (5, 5 + 105 * i, self.x - 10, 100), 5)

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 5 < self.mouse_x < 115 and self.y - 65 < self.mouse_y < self.y - 15:
            self.running = False
            Main()


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
        con = sqlite3.connect('/Users/elizavetabachurina/PycharmProjects/yandex_project_2-/DataBase/stat.db')
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
        pygame.init()
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









