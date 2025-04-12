from pygame import *




win_width = 700
win_height = 500

window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('ping-pong')
background = transform.scale(
    image.load('фон пинг-понга.jpg'),
    (win_width,win_height)
    )   

FPS = 60
game = True
finish = False










display.update()
