import pygame

flag = 0
class StartStateMenu:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = 800, 600

        pygame.init()
        pygame.display.set_caption('ээээ название игры')

        self.screen.fill('black')

        pygame.draw.rect(self.screen, (0, 150, 0), (230, 140, 340, 70), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (250, 220, 300, 50), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (250, 290, 300, 50), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (250, 360, 300, 50), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (250, 430, 300, 50), 0)
        pygame.draw.rect(self.screen, (0, 150, 0), (200, 10, 400, 120), 5)


        self.text_button()

        pygame.display.flip()


    def text_button(self):
        font = pygame.font.Font(None, 35)
        text = font.render("Начало новой игры", True, (255, 255, 255))
        text_x = 260
        text_y1 = 165
        self.screen.blit(text, (text_x, text_y1))

        font = pygame.font.Font(None, 28)
        text = font.render("Загрузить игру", True, (255, 255, 255))
        text_y2 = 235
        self.screen.blit(text, (text_x, text_y2))

        text = font.render("Сохранения", True, (255, 255, 255))
        text_y3 = 305
        self.screen.blit(text, (text_x, text_y3))

        text = font.render("Статистика", True, (255, 255, 255))
        text_y3 = 375
        self.screen.blit(text, (text_x, text_y3))

        text = font.render("Выход", True, (255, 255, 255))
        text_y3 = 445
        self.screen.blit(text, (text_x, text_y3))

        font = pygame.font.SysFont('serif', 60)
        text = font.render("The little world", True, (255, 255, 255))
        text_x0 = 215
        text_y = 50
        self.screen.blit(text, (text_x0, text_y))


class Buttons:
    def __init__(self, screen):
        self.screen = screen
        self.size = 800, 600
        self.click_buttons()

        pygame.display.flip()

    def click_buttons(self):
        global flag
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if flag == 0:
            if 250 <= mouse_x <= 550:
                if 220 <= mouse_y <= 270:
                    self.screen.fill('white')
                    pass

                elif 290 <= mouse_y <= 340:
                    pass

                elif 360 <= mouse_y <= 410:
                    flag = 2
                    self.screen.fill('black')

                    pass

                elif 430 <= mouse_y <= 480:
                    flag = 1
                    self.screen.fill('black')
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


                if 230 <= mouse_x <= 570 and 140 <= mouse_y <= 210:
                    pass

        elif flag == 1:
            if 160 <= mouse_x <= 360 and 350 <= mouse_y <= 400:
                pygame.quit()
                exit()

            elif 440 <= mouse_x <= 640 and 350 <= mouse_y <= 400:
                flag = 0
                StartStateMenu(self.screen)






