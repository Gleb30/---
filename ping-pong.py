from pygame import *

back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, width,height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))

class Player(GameSprite):    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

racket1 = Player('palka.png', 30,200,50,150,4)
racket2 = Player('palka.png',520, 200,50,150,4)
ball = GameSprite('tenis.png', 200,200,50,50,4)

font.init()
font1 = font.Font(None,35)
lose1 = font1.render('Player 1 Lose!',True,(180,0,0))
lose2 = font1.render('Player 2 Lose!',True,(180,0,0))

speed_x = 3
speed_y = 3

game = True
finish = False
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reest()
    display.update()
    clock.tick(FPS)

'''
display.set_caption('пинг-понг')
background = transform.scale(
    image.load('фон пинг-понга.jpg'),
    (win_width,win_height)
    )   
'''



