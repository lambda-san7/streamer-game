import pygame
import os 

pygame.init()

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

favicon = pygame.image.load(f"{dir_path}/switch logo.png")
icon = pygame.transform.scale(pygame.image.load(f"{dir_path}/switch logo.png"),(100,100))
menu_icon = pygame.transform.scale(pygame.image.load(f"{dir_path}/round invert logo.png"),(200,200))