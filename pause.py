from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *

janela = Window(1224,822)
mouse = Window.get_mouse()
teclado = keyboard.Keyboard()


def pause():
    pausar = Sprite("imagem/pause.png")
    pausar.x = janela.width / 2 - pausar.width / 2
    pausar.y = janela.height / 10

    voltar = Sprite("imagem/voltar.png")
    voltar.x = janela.width / 2 - voltar.width / 2
    voltar.y = janela.height /2

    voltarver = Sprite("imagem/voltarver.png")
    voltarver.x = janela.width / 2 - voltarver.width / 2
    voltarver.y = janela.height /2

    qt = Sprite("imagem/quit.png")
    qt.x = janela.width / 2 - qt.width / 2.3
    qt.y = janela.height /2 + 60

    qtred = Sprite("imagem/quitred.png")
    qtred.x = janela.width / 2 - qtred.width / 2.3
    qtred.y = janela.height /2 + 60

    while True:
        janela.set_background_color((0,0,0))

        if (mouse.is_over_object(qt)):
            qt.hide()
            qtred.draw()
            if (mouse.is_button_pressed(1)):
                return True
        else:
            qt.unhide()

        if (mouse.is_over_object(voltar)):
            voltar.hide()
            voltarver.draw()
            if (mouse.is_button_pressed(1)):
                return False
        else:
            voltar.unhide()
        
        pausar.draw()
        voltar.draw()
        qt.draw()
        janela.update()