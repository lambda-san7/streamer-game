########################
# IMPORTS
########################

import pygame
from assets import (
    dir_path,
    favicon,
    icon,
    menu_icon,
)

########################
# DEFAULT SHIT
########################

pygame.init()

window = pygame.display.set_mode((900,600),pygame.RESIZABLE)

pygame.display.set_caption("Stream")
pygame.display.set_icon(favicon)

running = True

fps = 60

clock = pygame.time.Clock()

########################
# TEXT
########################

class text:
    def __init__(self, size, text, color=(255,255,255)):
        self.font = pygame.font.Font(f"{dir_path}/font.ttf",size)
        self.color = color
        self.text_holder = text
        self.size_holder = size
        self.text = self.font.render(text, True, self.color)
        self.w = self.text.get_width()
        self.h = self.text.get_height()
    def render(self,x,y):
        self.font = pygame.font.Font(f"{dir_path}/font.ttf",self.size_holder)
        self.text = self.font.render(self.text_holder, True, self.color)
        window.blit(self.text,(x,y))

########################
# SCENES
########################

scene = None

class main_menu:
    def handle():
        window.fill((255,0,148))
        window.blit(menu_icon,((pygame.display.Info().current_w / 2) - 100,20))
        msg = text(32,"Start Streaming")
        if (pygame.mouse.get_pos()[0] < (pygame.display.Info().current_w / 2) - (msg.w / 2) + msg.w and
            pygame.mouse.get_pos()[0] > (pygame.display.Info().current_w / 2) - (msg.w / 2) and
            pygame.mouse.get_pos()[1] < 2.5 * 100 + msg.h and
            pygame.mouse.get_pos()[1] > 2.5 * 100):
            msg.color = (255,126,201)
            if pygame.mouse.get_pressed()[0]:
                print("clicked")
        msg.render((pygame.display.Info().current_w / 2) - (msg.w / 2), 2.5 * 100)

class main_menu:
    def handle():
        window.fill((255,0,148))
        window.blit(menu_icon,((pygame.display.Info().current_w / 2) - 100,20))
        msg = text(32,"Start Streaming")
        if (pygame.mouse.get_pos()[0] < (pygame.display.Info().current_w / 2) - (msg.w / 2) + msg.w and
            pygame.mouse.get_pos()[0] > (pygame.display.Info().current_w / 2) - (msg.w / 2) and
            pygame.mouse.get_pos()[1] < 2.5 * 100 + msg.h and
            pygame.mouse.get_pos()[1] > 2.5 * 100):
            msg.color = (255,126,201)
            if pygame.mouse.get_pressed()[0]:
                print("clicked")
        msg.render((pygame.display.Info().current_w / 2) - (msg.w / 2), 2.5 * 100)

########################
# GAME LOOP
########################

scene = main_menu

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    scene.handle()
    pygame.display.update()

pygame.quit