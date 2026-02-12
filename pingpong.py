from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, imagep, x,y,speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(imagep), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class racket(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < (height - 150):
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < (height - 150):
            self.rect.y += self.speed
width = 600
back_color = (200,255,255)
height = 500
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
rocket1 = racket('racket.png',70,200,10,30,130)
rocket2 = racket('racket.png',500,300,10,30,130)
font.init()
fontik = font.Font('CGXYZPCAlt-Regular.otf', 10)
loser1 = fontik.render('1ST PLAYER LOST!', True,(200,0,0))
loser2 = fontik.render('2ND PLAYER LOST!', True,(200,0,0))
ball = GameSprite('tenis_ball.png', 250,250,5,60,60)
clock = time.Clock()
FPS = 60
game = True
finish = False
ballIX = 4
ballIY = 4
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back_color)
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += ballIX
        ball.rect.y += ballIY
        if sprite.collide_rect(rocket1,ball):
            ballIX *= -1
        if sprite.collide_rect(rocket2,ball):
            ballIX *= -1
        if ball.rect.y < 0 or ball.rect.y > (height-50):
            ballIY *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loser1,(250,250))
        if ball.rect.x > (width - 50):
            finish = True
            window.blit(loser2,(250,250))
        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)