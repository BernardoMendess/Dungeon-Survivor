from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sound import *
from game import jogo
from ranking import tela_ranking

janela = Window(1224,822)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()
som = Sound("som/Somdefundo.ogg")
som.set_volume(10)

logo = Sprite("imagem/lg.png")
logo.x = janela.width/2 - logo.width/2
logo.y = 100

fundo = GameImage("imagem/fundo.png")

start = Sprite("imagem/strt.png")
start.x = janela.width/2 - start.width/2
start.y = janela.height/1.53+50

startred = Sprite("imagem/strtred.png")
startred.x = janela.width/2 - startred.width/2
startred.y = janela.height/1.53+50

rank = Sprite("imagem/rank.png")
rank.x = janela.width/2 - rank.width/2
rank.y = janela.height/1.38+50

rankred = Sprite("imagem/rankred.png")
rankred.x = janela.width/2 - rankred.width/2
rankred.y = janela.height/1.38+50

qt = Sprite("imagem/quit.png")
qt.x = janela.width/2 - qt.width/2.3
qt.y = janela.height/1.25+50

qtred = Sprite("imagem/quitred.png")
qtred.x = janela.width/2 - qtred.width/2.3
qtred.y = janela.height/1.25+50

while True:
    janela.set_background_color((0, 0, 0))
    fundo.draw()

    if (mouse.is_over_object(start)):
        start.hide()
        startred.draw()
        if (mouse.is_button_pressed(1)):
            dif = 200
            som.stop()
            jogo(dif, True)
    else:
        start.unhide()

    if (mouse.is_over_object(rank)):
        rank.hide()
        rankred.draw()
        if (mouse.is_button_pressed(1)):
            point = [-1]
            tela_ranking(point)
    else:
        rank.unhide()

    if (mouse.is_over_object(qt)):
        qt.hide()
        qtred.draw()
        if (mouse.is_button_pressed(1)):
            break
    else:
        qt.unhide()

    logo.draw()
    start.draw()
    rank.draw()
    qt.draw()
    som.play()
    janela.update()