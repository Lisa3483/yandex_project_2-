import pygame


class StartMenu:
    def __init__(self):
        size = 800, 600
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('ээээ название игры')

        pygame.draw.rect(screen, (0, 150, 0), (230, 140, 340, 70), 0)
        pygame.draw.rect(screen, (0, 150, 0), (250, 220, 300, 50), 0)
        pygame.draw.rect(screen, (0, 150, 0), (250, 290, 300, 50), 0)
        pygame.draw.rect(screen, (0, 150, 0), (250, 360, 300, 50), 0)
        pygame.draw.rect(screen, (0, 150, 0), (250, 430, 300, 50), 0)
        pygame.draw.rect(screen, (0, 150, 0), (250, 500, 300, 50), 0)
        pygame.draw.rect(screen, (0, 150, 0), (200, 10, 400, 120), 5)

        self.text_button(screen)

        pygame.display.flip()



    def text_button(self, screen):
        font = pygame.font.Font(None, 35)
        text = font.render("Начало новой игры", True, (255, 255, 255))
        text_x = 260
        text_y = 165
        screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 28)
        text = font.render("Загрузить игру", True, (255, 255, 255))
        text_y = 235
        screen.blit(text, (text_x, text_y))

        text = font.render("Сохранения", True, (255, 255, 255))
        text_y = 305
        screen.blit(text, (text_x, text_y))

        text = font.render("Настройки", True, (255, 255, 255))
        text_y = 375
        screen.blit(text, (text_x, text_y))

        text = font.render("Статистика", True, (255, 255, 255))
        text_y = 445
        screen.blit(text, (text_x, text_y))

        text = font.render("Выход", True, (255, 255, 255))
        text_y = 515
        screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 100)
        text = font.render("Название", True, (255, 255, 255))
        text_x = 215
        text_y = 50
        screen.blit(text, (text_x, text_y))

