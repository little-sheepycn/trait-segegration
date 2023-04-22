import pygame,random
from pygame import *
init()
pygame.freetype.init()
D_D=image.load("resources/pea/D_D.png")
D_d=image.load("resources/pea/D_d.png")
d_d=image.load("resources/pea/d_d.png")
D_D_original=image.load("resources/pea/D_D_original.png")
D_d_original=image.load("resources/pea/D_d_original.png")
d_d_original=image.load("resources/pea/d_d_original.png")
gamefont=pygame.freetype.Font("resources/fonts/unifont.ttf",26)
screen = display.set_mode((1280,720))
pygame.display.set_caption("分离定律模拟")
running=True
clock=time.Clock()
screen.fill('#66CCFF')
banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
Apressed=False
num=""
def get_text(press,txt):
    if press[pygame.K_0]:
        txt=txt+"0"
    if press[pygame.K_1]:
        txt=txt+"1"
    if press[pygame.K_2]:
        txt=txt+"2"
    if press[pygame.K_3]:
        txt=txt+"3"
    if press[pygame.K_4]:
        txt=txt+"4"
    if press[pygame.K_5]:
        txt=txt+"5"
    if press[pygame.K_6]:
        txt=txt+"6"
    

while running:
    for event in pygame.event.get():
        if event.type ==QUIT:
            running=False
    clock.tick(60)
    keys=key.get_pressed()
    if keys[pygame.K_a]:
        Apressed=True
    if Apressed == False:
        pressA=gamefont.render_to(screen,(540,360),"PRESS A TO START")
    else:
        screen.fill('#66CCFF')
        banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
        notify=gamefont.render_to(screen,(540,360),"请输入豌豆数量:")
        display.flip()
        if keys[pygame.K_0]:
            num=num+"0"
        if keys[pygame.K_1]:
            num=num+"1"
        if keys[pygame.K_2]:
            num=num+"2"

    display.flip()
