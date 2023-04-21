import pygame
from pygame import *
def initpygame():
    init()
    pygame.freetype.init()
def loadres():
    D_D=image.load("resources/pea/D_D.png")
    D_d=image.load("resources/pea/D_d.png")
    d_d=image.load("resources/pea/d_d.png")
    D_D_original=image.load("resources/pea/D_D_original.png")
    D_d_original=image.load("resources/pea/D_d_original.png")
    d_d_original=image.load("resources/pea/d_d_original.png")
    font=pygame.freetype.Font("unifont.ttf",26)
initpygame()
screen = display.set_mode((1280,720))
running=True
clock=time.Clock()
screen.fill('#66CCFF')
while running:
    for event in pygame.event.get():
        if event.type ==QUIT:
            running=False
    clock.tick(60)
    loadres()
    banner=font.render_to(screen,(320,100),"分离定律模拟")
    display.flip()
