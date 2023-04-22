import pygame,random,time
#from pygame import *
pygame.init()
pygame.freetype.init()
trait=["D","d"]
result={'DD':0,'dd':0,'Dd':0}
D_D=pygame.image.load("resources/pea/D_D.png")
D_d=pygame.image.load("resources/pea/D_d.png")
d_d=pygame.image.load("resources/pea/d_d.png")
D_D_original=pygame.image.load("resources/pea/D_D_original.png")
D_d_original=pygame.image.load("resources/pea/D_d_original.png")
d_d_original=pygame.image.load("resources/pea/d_d_original.png")
gamefont=pygame.freetype.Font("resources/fonts/unifont.ttf",26)
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("分离定律模拟")
running=True
clock=pygame.time.Clock()
screen.fill('#66CCFF')
banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
screen.blit(D_D_original,(300,500))
screen.blit(D_d_original,(480,500))
screen.blit(d_d_original,(660,500))
Apressed=False
bpressed=False
input_finish=False
num=""
'''
def get_text(press,txt):
    if press[pygame.K_0]:
        txt=txt+"0"
    elif press[pygame.K_1]:
        txt=txt+"1"
    elif press[pygame.K_2]:
        txt=txt+"2"
    elif press[pygame.K_3]:
        txt=txt+"3"
    elif press[pygame.K_4]:
        txt=txt+"4"
    elif press[pygame.K_5]:
        txt=txt+"5"
    elif press[pygame.K_6]:
        txt=txt+"6"
    elif press[pygame.K_7]:
        txt=txt+"7"
    elif press[pygame.K_8]:
        txt=txt+"8"
    elif press[pygame.K_9]:
        txt=txt+"9"
'''
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
    clock.tick(60)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Apressed=True
    if Apressed == False:
        pressA=gamefont.render_to(screen,(540,360),"PRESS A TO START")
    if Apressed == True:

        #get_text(keys,num)
        if input_finish == False:
            screen.fill('#66CCFF')
            banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
            notify=gamefont.render_to(screen,(500,360),"请在终端窗口中输入豌豆数量:")
            screen.blit(D_D_original,(300,500))
            screen.blit(D_d_original,(480,500))
            screen.blit(d_d_original,(660,500))
            pygame.display.flip()
            num=input("在此输入豌豆数量：")
            input_finish=True
        else:
            if bpressed==False:
                screen.fill('#66CCFF')
                banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
                numbers=gamefont.render_to(screen,(530,360),"按下B以确认输入："+num)
                screen.blit(D_D_original,(300,500))
                screen.blit(D_d_original,(480,500))
                screen.blit(d_d_original,(660,500))
                pygame.display.flip()
                if pygame.key.get_pressed()[pygame.K_b]:
                    notify_calc=gamefont.render_to(screen,(540,360),"正在计算")
                    calc_input=int(num)
                    bpressed=True
                    for i in range(calc_input):
                        trait1=random.choice(trait)
                        trait2=random.choice(trait)
                        gene=trait1+trait2
                        if gene=='DD':
                            result["DD"]+=1
                            screen.fill('#66CCFF')
                            banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
                            notify_calc=gamefont.render_to(screen,(540,360),"正在计算")
                            screen.blit(D_D,(300,500))
                            screen.blit(D_d_original,(480,500))
                            screen.blit(d_d_original,(660,500))
                            pygame.display.flip()
                            time.sleep(0.01)
                        elif gene=='dd':
                            result["dd"]+=1
                            screen.fill('#66CCFF')
                            banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
                            notify_calc=gamefont.render_to(screen,(540,360),"正在计算")
                            screen.blit(D_D_original,(300,500))
                            screen.blit(D_d_original,(480,500))
                            screen.blit(d_d,(660,500))
                            pygame.display.flip()
                            time.sleep(0.01)
                        else:
                            result["Dd"]+=1
                            screen.fill('#66CCFF')
                            banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
                            notify_calc=gamefont.render_to(screen,(540,360),"正在计算")
                            screen.blit(D_D_original,(300,500))
                            screen.blit(D_d,(480,500))
                            screen.blit(d_d_original,(660,500))
                            pygame.display.flip()
                            time.sleep(0.01)
            if bpressed==True:
                screen.fill('#66CCFF')
                banner=gamefont.render_to(screen,(540,100),"分离定律模拟",size=36)
                notify_finish=gamefont.render_to(screen,(200,360),"结果:")
                result_D_D=gamefont.render_to(screen,(260,360),"D D:"+str(result.get("DD")))
                result_D_d=gamefont.render_to(screen,(result_D_D.x+result_D_D.width+10,360),"D d:"+str(result.get('Dd')))
                result_d_d=gamefont.render_to(screen,(result_D_d.x+result_D_d.width+10,360),"d d:"+str(result.get('dd')))
                pygame.display.flip()

    pygame.display.flip()
