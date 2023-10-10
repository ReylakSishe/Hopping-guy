import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("usted ha usado el click izquierdo")
    elif button == mouse.RIGHT:
        print("usted ha usado el click derecho")
    elif button == mouse.MIDDLE:
        print("usted ha usado el click medio")

pyglet.app.run()