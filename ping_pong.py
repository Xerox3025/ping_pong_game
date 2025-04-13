from pygame import *
from random import uniform, randint, randrange
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (width,height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.y += self.speed
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

back = (100,100,100)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

display.set_caption("Ping Pong")

player1 = Player('bullet.png',30,200,6,50,150)
player2 = Player('bullet.png',520,200,6,50,150)
ball = GameSprite('asteroid.png',200,200,4,50,50)

game = True
finish = False
clock = time.Clock()
FPS = 60

player1_score = 0
player2_score = 0

font.init()
font2 = font.Font(None,35)
lose2 = font2.render("PLAYER2 LOSE",True,(255,255,255))
lose1 = font2.render("PLAYER1 LOSE",True,(255,255,255))

wid = 50
heig = 50

num = [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]
speed_x = num[randint(0,11)]
speed_y = num[randint(0,11)]
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        player1.update_l()
        player2.update_r()

        player1.reset()
        player2.reset()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
        speed_x *= -1
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0: 
        speed_x = num[randint(0,11)]
        speed_y = num[randint(0,11)]
        player2_score += 1
        wid -= 1
        heig -= 1
        ball = GameSprite('asteroid.png',200,200,4,wid,heig)
        

    if ball.rect.x > win_width-60:
        speed_x = num[randint(0,11)]
        speed_y = num[randint(0,11)]
        player1_score += 1
        wid -= 1
        heig -= 1
        ball = GameSprite('asteroid.png',200,200,4,wid,heig)
        

    if player1_score >= 10:
        finish = True
        window.blit(lose2,(200,200))
        game_over = True

    if player2_score >= 10:
        finish = True
        window.blit(lose1,(200,200))
        game_over = True
    
    speed_x *= 1.002
    speed_y *= 1.002
    

    text1 = font2.render('Player1: ' + str(player1_score),1,(255,255,255))
    window.blit(text1,(10,20))
    text2 = font2.render('Player2: ' + str(player2_score),1,(255,255,255))
    window.blit(text2,(400,20))
    
    display.update()
    clock.tick(FPS)
