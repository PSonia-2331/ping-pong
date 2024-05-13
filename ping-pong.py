from pygame import * 

font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

lose_l = font1.render("Игрок слева проиграл!", True, (180, 0, 0))
lose_r = font1.render('Игрок справа проиграл!', True, (180, 0, 0))

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (wigth, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:

            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.x > 5:

            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

  


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

racket1 = Player('qqq.png', 30, 200, 4, 60, 150)
racket2 = Player('qqq.png', 520, 200, 4, 60, 150)
boll = GameSprite('boll.png', 200, 200, 4, 50, 50)


speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        boll.rect.x += speed_x
        boll.rect.y += speed_y

        if sprite.collide_rect(racket1, boll) or sprite.collide_rect(racket2, boll):
            speed_x *= -1
            speed_y *= 1

        if boll.rect.y > win_height-50 or boll.rect.y < 0:
            speed_y *= -1

        if boll.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if boll.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        boll.reset()

    display.update()
    clock.tick(FPS)