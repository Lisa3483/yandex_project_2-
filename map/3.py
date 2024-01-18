import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

tileset_image = pygame.image.load('images/tileset2.bmp')

tile_width = 16
tile_height = 16

level_map = [
    [96, 96, 96, 96, 96, 96, 96, 100],
    [88, 88, 88, 88, 88, 88, 88, 92],
    [80, 78, 79, 80, 78, 85, 88, 92],
    [70, 68, 69, 70, 68, 85, 88, 92],
    [60, 58, 59, 60, 58, 85, 88, 92],
    [52, 50, 51, 52, 50, 85, 88, 92],
    [96, 96, 96, 96, 96, 96, 88, 92],
    [88, 88, 88, 88, 88, 88, 88, 92],
    [88, 88, 88, 88, 88, 88, 88, 92]
]

for y, row in enumerate(level_map):
    for x, tile in enumerate(row):
        tile_rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)
        screen.blit(tileset_image, tile_rect, area=(tile * tile_width, 0, tile_width, tile_height))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
