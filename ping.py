from pygame import *



class GameSprite(sprite.Sprite):
    # amogus
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def amogus(self):
        pass


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y = self.rect.y - self.speed

        if keys[K_s] and self.rect.y < win_width - 50:
            self.rect.y = self.rect.y + self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y = self.rect.y - self.speed

        if keys[K_DOWN] and self.rect.y < win_width - 50:
            self.rect.y = self.rect.y + self.speed

back = (200, 255, 255) # цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

player1 = Player("racket.png", 50, 250, 4, 50, 150)
player2 = Player("racket.png", win_width - 50, 250, 4, 50, 150)

ball = GameSprite("tenis_ball.png", 200, 200, 50, 50, 4)

color = (169,169,169)
win_width = 600
win_height = 500

window = display.set_mode((win_height, win_height))
window.fill(color)

#флаги отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    player1.update_l()
    player1.reset()

    player2.update_r()
    player2.reset()

    display.update()
    clock.tick(FPS)