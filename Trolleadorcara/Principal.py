import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window(1280, 720)


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
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("usted ha usado el click izquierdo")
    elif button == mouse.RIGHT:
        print("usted ha usado el click derecho")
    elif button == mouse.MIDDLE:
        print("usted ha usado el click medio")


Rickroll = pyglet.resource.media(
    "Recursos/Musica/Rick Astley - Never Gonna Give You Up (Official Music Video).mp4",
)

Reproductor = pyglet.media.Player()
Reproductor.queue(Rickroll)


@window.event
def on_draw():
    window.clear()
    Reproductor.get_texture().blit(0, 0)


Reproductor.play()

pyglet.app.run()
