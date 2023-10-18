import pyglet

window = pyglet.window.Window(1280, 720)

Rickroll = pyglet.media.load(
    "/home/reylak/Documentos/GitHub/Hopping-guy/Trolleadorcara/Scripts/SQL Lite/Rick Astley - Never Gonna Give You Up (Official Music Video).mp4",
)

Reproductor = pyglet.media.Player()
Reproductor.queue(Rickroll)


@window.event
def on_draw():
    window.clear()
    Reproductor.get_texture().blit(0, 0)


Reproductor.play()

pyglet.app.run()
