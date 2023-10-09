import pyglet
from pyglet.window import key

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('La tecla A ha sido presionada.')
    elif symbol == key.LEFT:
        print('La tecla Izquierda ha sido presionada.')
    elif symbol == key.ENTER:
        print('La tecla Enter ha sido presionada.')
    elif symbol == key.P:
        print('La tecla P ha sido presionada')
    elif symbol == key.RIGHT:
        print('La tecla Derecha ha sido presionada')
    elif symbol == key.TAB:
        print('La tecla Tab ha sido')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()