import pyglet
from pyglet.window import key

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        print('La tecla "Arriba" ha sido presionada.')
    elif symbol == key.LEFT:
        print('La tecla "Izquierda" ha sido presionada.')
    elif symbol == key.DOWN:
        print('La tecla "Abajo" ha sido presionada.')
    elif symbol == key.RIGHT:
        print('La tecla "Derecha" ha sido presionada')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()