import pygame

flag = 4


class Exit:
    def __init__(self, screen, menu):
        self.screen = screen
        self.menu = menu
        self.x, self.y = 800, 600
        self.flag = 4

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

        pygame.draw.rect(self.screen, (153, 102, 51), (100, 100, 600, 400), 8)
        pygame.draw.rect(self.screen, (255, 255, 255), (98, 98, 604, 404), 2)
        pygame.draw.rect(self.screen, (255, 255, 255), (108, 108, 584, 384), 2)

        font = pygame.font.Font(None, 40)
        text = font.render("Вы точно хотите выйти?", True, (255, 255, 255))
        self.screen.blit(text, (240, 140))

        pygame.draw.rect(self.screen, (153, 102, 51), (160, 350, 200, 50), 0)
        pygame.draw.rect(self.screen, (153, 102, 51), (440, 350, 200, 50), 0)
        pygame.draw.rect(self.screen, (255, 255, 255), (158, 348, 204, 54), 2)
        pygame.draw.rect(self.screen, (255, 255, 255), (438, 348, 204, 54), 2)

        font = pygame.font.Font(None, 40)

        text = font.render("ДА", True, (255, 255, 255))
        self.screen.blit(text, (230, 360))

        text = font.render("НЕТ", True, (255, 255, 255))
        self.screen.blit(text, (510, 360))
        pygame.display.flip()

    def flagg(self):
        return self.flag

    def buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if 160 <= self.mouse_x <= 360 and 350 <= self.mouse_y <= 400:
            pygame.quit()
            exit()

        elif 440 <= self.mouse_x <= 640 and 350 <= self.mouse_y <= 400:
            if self.menu == 'start':
                self.flag = 1
            else:
                self.flag = 10
