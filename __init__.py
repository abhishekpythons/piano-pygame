import pygame
pygame.init()
keys='`1234567890-=qwertyuiop[asdfghjkl;zxcvbnm,.'
buttons={}
for i in range(1,89):
    buttons[i]=pygame.mixer.Sound('KEY(%d).WAV'%i)
scr=pygame.display.set_mode((500,500))
font=pygame.font.Font('freesansbold.ttf',30)
label1=font.render('PRESS KEYS FROM 0-9,A-Z,a-z',1,(255,0,0))
label2=font.render('To Play Piano',1,(0,255,0))
time=0
game=True
pressed=not game
a=pygame.mixer.Channel(0)
b=pygame.mixer.Channel(1)
while game:
    #scr.fill((255,255,255)) =>  scr.fill(255*255*255*129+8486272)
    scr.fill(1290**3)
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            game=False
        if eve.type==pygame.KEYDOWN:
            if len(eve.unicode)>0 and eve.unicode.lower() in keys:
                play=keys.index(eve.unicode.lower()) +45 if eve.mod==pygame.KMOD_CAPS else keys.index(eve.unicode)+1
                if a.get_busy() and b.get_busy():
                    a.stop()
                if a.get_busy():
                    b.play(buttons[play])
                else:
                    a.play(buttons[play])
                pressed=eve.unicode
                label3=font.render(f'PRESSED {eve.unicode}',1,(0,0,255),(0,255,0))
                label4=font.render(f'PLAYING KEY({play})',1,(0,255,0),(0,0,255))
        if eve.type==pygame.KEYUP:
            pressed=None 
    scr.blit(label1,(250-label1.get_size()[0]//2,0))
    scr.blit(label2,(250-label2.get_size()[0]//2,50))
    if pressed:
        scr.blit(label3,(250-label3.get_size()[0]//2,250-label3.get_size()[1]//2)) 
        scr.blit(label4,(250-label4.get_size()[0]//2,250-label4.get_size()[1]//2+50))
#    print('YES' if capslock!=0 else 'NO')
    pygame.display.update()
pygame.quit()
