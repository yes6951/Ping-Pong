from pygame import *
from random import randint as rt


'''Необходимые классы'''

# класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


back = (200, 255, 255)  # цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

# флаги отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

# создание мяча и ракеток coins🤑🤑
player1 = Player('racket.png', 30, 200, 4, 50, 150)
player2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
coin = GameSprite('coin.png', rt(50, win_width - 50), rt(50, win_height - 50), 0, 50, 50)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        player1.update_l()
        player2.update_r()
        coin.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y >= win_height - 50 or ball.rect.y <= 50:
            speed_x *= 1
            speed_y *= -1


        player1.reset()
        player2.reset()
        ball.reset()
        coin.reset()

    display.update()
    clock.tick(FPS)