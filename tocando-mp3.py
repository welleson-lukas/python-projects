"""
TOCAR MUSICA
"""

import pygame
pygame.init()
pygame.mixer.music.load('tocar.mp3')
pygame.mixer.music.play()
pygame.event.wait()


