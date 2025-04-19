from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, width,height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    



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
