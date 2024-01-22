import pygame


flag = True
color = (153, 102, 51)


class StartStateMenu:
    def __init__(self, screen):
        self.mouse_x, self.mouse_y = 0, 0
        self.flag = 1
        self.screen = screen
        self.x, self.y = 800, 600


    def okno(self):
        global color
        image = pygame.image.load('images/sstone.jpeg').convert_alpha()
        new_image = pygame.transform.scale(image, (self.x, self.y))
        self.screen.blit(new_image, (0, 0))

        for i in range(4):
            pygame.draw.rect(self.screen, color, (250, 160 + i * 70, 300, 50), 0)
            pygame.draw.rect(self.screen, (255, 255, 255), (250 - 2, 160 + i * 70 - 2, 304, 54), 2)

        pygame.draw.rect(self.screen, (153, 102, 51), (200, 10, 400, 120), 8)
        pygame.draw.rect(self.screen, (255, 255, 255), (200 - 1, 10 - 1, 402, 122), 1)
        pygame.draw.rect(self.screen, (255, 255, 255), (208, 18, 384, 104), 1)

        self.text_button()

        pygame.display.flip()


    def all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                Buttons(self.screen, self.mouse_x, self.mouse_y)

    def text_button(self):
        words = ["Начало новой игры", "Сохранения", "Статистика", "Выход"]

        font = pygame.font.Font(None, 28)

        for i in words:
            text = font.render(i, True, (255, 255, 255))
            w = text.get_rect().width
            text_y = 175 + words.index(i) * 70
            self.screen.blit(text, (250 + 150 - w // 2, text_y))

        font = pygame.font.SysFont('serif', 60)
        text = font.render("The little world", True, (255, 255, 255))
        text_x0 = 215
        text_y = 50
        self.screen.blit(text, (text_x0, text_y))

    def flagg(self):
        return Buttons(self.screen, self.mouse_x, self.mouse_y).flagss()


class Buttons:
    def __init__(self, screen, mouse_x, mouse_y):
        self.flag = 1
        self.screen = screen
        self.x, self.y = 800, 600
        self.click_buttons(mouse_x, mouse_y)

    def click_buttons(self, mouse_x, mouse_y):
        if 250 <= mouse_x <= 550:
            if 220 <= mouse_y <= 270:
                self.flag = 2

            elif 290 <= mouse_y <= 340:
                self.flag = 3

            elif 360 <= mouse_y <= 410:
                self.flag = 4

            elif 160 <= mouse_y <= 210:
                self.flag = 5

    def flagss(self):
        return self.flag


