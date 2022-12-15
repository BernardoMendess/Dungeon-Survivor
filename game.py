from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.sound import *
from ranking import tela_ranking
from random import randint
from pause import pause


janela = Window(1224,822)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
point = [0]
tochas = [0]
vidas = [0]
som_moeda = Sound("som/moedasom.ogg")
som_moeda.set_volume(5)
som_tocha = Sound("som/tocha_som.ogg")
som_tocha.set_volume(5)
som_player = Sound("som/som_morte_player.ogg")
som_player.set_volume(15)
som_fan = Sound("som/som_morte_fantasma.ogg")
som_fan.set_volume(30)
NC = [0]


def cria_matriz(matriz, moeda, fundo):
    for a in range(16):
        for b in range(16):
            if matriz[a][b] == 0:
                moeda = Sprite("imagem/moeda.png")
                moeda.set_position(212+b*50+16,11+a*50+16)
                matriz[a][b] = moeda
            elif matriz[a][b] == 1:
                fundo = Sprite("imagem/pt2.png")
                fundo.set_position(212+b*50,11+a*50)
                matriz[a][b] = fundo
            elif matriz[a][b] == 2:
                tocha = Sprite("imagem/tocha.png")
                tocha.set_position(212+b*50,11+a*50)
                matriz[a][b] = tocha

def desenha_moedas(matriz):
    for a in range(16):
        for b in range(16):
            if matriz[a][b] != "VAZIO":
                matriz[a][b].draw()

def colisao(matriz, gue, ME):
    for a in range(16):
        for b in range(16):
            if matriz[a][b] != "VAZIO":
                if gue.collided(matriz[a][b]):
                    if ME[a][b] == 0:
                        matriz[a][b] = "VAZIO"
                        point[0] = point[0]+1
                        som_moeda.play()
                        NC[0] = NC[0]+1
                        return 1
                    if ME[a][b] == 1:
                        return -1
                    if ME[a][b] == 2:
                        som_tocha.play()
                        matriz[a][b] = "VAZIO"
                        if tochas[0] < 3:
                            tochas[0] = tochas[0]+1
    return 0


def jogo(dif, inicio):
    dif = dif-10
    matriz = [
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0],
    [1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,0,"VAZIO",0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0],
    [0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0],
    [1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ]

    ME = [
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0],
    [1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [0,0,0,0,0,"VAZIO",0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0],
    [0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0],
    [1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ]

    tocha = 0
    while True:
        a = randint(0,15)
        b = randint(0,15)
        if matriz[a][b] == 0:
            tocha += 1
            matriz[a][b] = 2
            ME[a][b] = 2
        if tocha == 3:
            break
    
    fundo = Sprite("imagem/pt2.png")

    gue = Sprite("imagem/guerreiro.png", 16)
    gue.set_total_duration(5000)
    gue.x = 462
    gue.y = 461

    fan1 = Sprite("imagem/fantasma.png")
    fan1.x = 512
    fan1.y = 361

    borda = Sprite("imagem/borda.png")
    borda.set_position(200, 0)

    cantoe = Sprite("imagem/canto.png")
    cantoe.set_position(0,0)

    cantod = Sprite("imagem/canto.png")
    cantod.set_position(janela.width-200,0)

    moeda = Sprite("imagem/moeda.png")

    mud = False
    dir = 0
    ndir = 0

    luz = 0

    cd = 0
    mf = False
    st = 0
    destinox = gue.x
    destinoy = gue.y

    tempo = 0
    cont = 0
    FPS = 0

    a = False

    imortalidade = 200
    
    cria_matriz(matriz, moeda, fundo)

    tochas[0] = 2
    vidas[0] = 3

    while True:
        if inicio == True:
            point[0] = 0
            NC[0] = 0
            inicio = False

        if gue.x > janela.width-gue.width/2-200:
            gue.set_position(200-gue.width/2,janela.height/2-50)
        elif gue.x < 200-gue.width/2:
            gue.set_position(janela.width-gue.width/2-200,janela.height/2-50)

        #escolhe direçao para andar
        adir = dir
        if(teclado.key_pressed("UP")):
            if(mud):
                gue.set_sequence(4,8, True)
            if(dir != 1):
                mud = True
            else:
                mud = False
            ndir = 1

        if (teclado.key_pressed("DOWN")):
            if(mud):
                gue.set_sequence(0,4, True)
            if(dir != 2):
                mud = True
            else:
                mud = False
            ndir = 2

        if (teclado.key_pressed("LEFT")):
            if(mud):
                gue.set_sequence(8,12, True)
            if(dir != 3):
                mud = True
            else:
                mud = False
            ndir = 3

        if (teclado.key_pressed("RIGHT")):
            if(mud):
                gue.set_sequence(12,16, True)
            if(dir != 4):
                mud = True
            else:
                mud = False
            ndir = 4

        dir = ndir

        #anda com o personagem
        if dir == 1 and gue.y > 11:
            gue.move_y(-1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_y(1)
                dir = adir
                if dir == 3 and (gue.x > 212 or gue.y == janela.height / 2 - 50):
                    gue.move_x(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(1)
                if dir == 4 and (gue.x < janela.width - gue.width - 212 or gue.y == janela.height / 2 - 50):
                    gue.move_x(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(-1)

        elif dir == 2 and gue.y < janela.height - gue.height - 11:
            gue.move_y(1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_y(-1)
                dir = adir
                if dir == 3 and (gue.x > 212 or gue.y == janela.height / 2 - 50):
                    gue.move_x(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(1)
                if dir == 4 and (gue.x < janela.width - gue.width - 212 or gue.y == janela.height / 2 - 50):
                    gue.move_x(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_x(-1)

        elif dir == 3 and (gue.x > 212 or gue.y == janela.height / 2 - 50):
            gue.move_x(-1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_x(1)
                dir = adir
                if dir == 1 and gue.y > 11:
                    gue.move_y(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(1)
                if dir == 2 and gue.y < janela.height - gue.height - 11:
                    gue.move_y(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(-1)

        elif dir == 4 and (gue.x < janela.width - gue.width - 212 or gue.y == janela.height / 2 - 50):
            gue.move_x(1)
            if colisao(matriz, gue, ME) == -1:
                gue.move_x(-1)
                dir = adir
                if dir == 1 and gue.y > 11:
                    gue.move_y(-1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(1)
                if dir == 2 and gue.y < janela.height - gue.height - 11:
                    gue.move_y(1)
                    if colisao(matriz, gue, ME) == -1:
                        gue.move_y(-1)


        #movimentaçao do fantasma
        if cd == 100+dif:
            if dif > 0:
                destinox = gue.x+randint(0,dif)
                destinoy = gue.y+randint(0,dif)
            cd = 0
        cd += 1


        if fan1.x >= janela.width-fan1.width-212 or fan1.x <= 212 or fan1.y >= janela.height-fan1.height-11 or fan1.y <= 11:
            cd = 100+dif
            if fan1.x >= janela.width-fan1.width-212:
                fan1.x -= 2
            if fan1.x <= 212:
                fan1.x += 2
            if fan1.y >= janela.height-fan1.height-11:
                fan1.y -= 2
            if fan1.y <= 11:
                fan1.y += 2


        #spaw cd
        if st == 400:
            mf = True
            st = 0
        
        #move
        if mf == True:
            if fan1.x < destinox and fan1.x < janela.width-fan1.width-212:
                fan1.move_x(1)
            elif fan1.x > destinox and fan1.x > 212:
                fan1.move_x(-1)
            if fan1.y < destinoy and fan1.y > 11:
                fan1.move_y(1)
            elif fan1.y > destinoy and fan1.y < janela.height-fan1.height-11:
                fan1.move_y(-1)
        else:
            st += 1


        #imortalidade
        if imortalidade > 0:
            imortalidade -= 1
        
        if imortalidade%2 == 0:
            gue.unhide()
        else:
            gue.hide()

        #colisao player - fantasma
        if imortalidade == 0:
            if gue.collided(fan1):
                gue.set_position(462,461)
                vidas[0] = vidas[0]-1
                som_player.play()
                imortalidade = 200
                if vidas[0] == 0:
                    inicio = True
                    if tela_ranking(point):
                        break


        #colisao fantasma - luz
        if luz != 0 and fan1.collided(circulo_luz):
            som_fan.play()
            fan1.set_position(462,361)
            st = 0
            mf = False

        #liga tocha
        if (teclado.key_pressed("SPACE")) and luz == 0:
            if tochas[0] > 0:
                tochas[0] = tochas[0]-1
                luz += 1
        
        if luz != 0:
            luz += 1
            if luz == 500:
                luz = 0

        #reinicia o jogo
        if NC[0] == 149:
            NC[0] = 0
            return jogo(dif, False)
        
        #sair do jogo
        if (teclado.key_pressed("ESC")):
            a = pause()
            if a:
                break

        #FPS
        tempo += janela.delta_time()
        cont += 1
        if tempo >= 1:
            tempo = 0
            FPS = cont
            cont = 0

        #draw
        janela.set_background_color((15, 15, 15))
        desenha_moedas(matriz)
        borda.draw()
        gue.update()
        gue.draw()
        fan1.draw()
        if luz != 0:
            circulo_luz = Sprite("imagem/luz.png")
            circulo_luz.set_position(gue.x-circulo_luz.width/2+gue.width/2,gue.y-circulo_luz.width/2+gue.width/2)
            circulo_luz.draw()
        cantoe.draw()
        cantod.draw()
        for i in range(tochas[0]):
            tocha = Sprite("imagem/tocha.png")
            tocha.set_position(1050+50*(i), 120)
            tocha.draw()
        for i in range(vidas[0]):
            vida = Sprite("imagem/vida.png")
            vida.set_position(1050+50*(i), 40)
            vida.draw()
        janela.draw_text(str(point[0]), 20, 20, size=48, font_name="Arial", bold=True, color=[255, 255, 255])
        janela.draw_text(str(FPS), 10, janela.height-50, size=25, color=(255, 255, 255))
        janela.update()