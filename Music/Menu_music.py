import pygame


class Music:
    def __init__(self):
        pygame.mixer.music.load('Music/sound.mp3')
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()