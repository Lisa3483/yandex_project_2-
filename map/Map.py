def mapp(pygame):
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Карта")

    white = (255, 255, 255)
    pygame.draw.line(screen, white, (0, 0), (width, height), 5)
    pygame.draw.line(screen, white, (0, height), (width, 0), 5)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
