import pygame 
okno = pygame.display.set_mode((1500, 800))
from random import *
clock = pygame.time.Clock()
pygame.init()
image_generator = pygame.font.Font(None, 50)
class Player():
    def __init__ (self, x, y, speed):
        self.hitbox = pygame.Rect(x, y, 50, 200)
        self.speed = speed
        self.score1 = 0
        self.score2 = 0
        self.score1_img = image_generator.render(str(self.score1), True, (100, 200, 50), (200, 100, 400))
        self.score2_img = image_generator.render(str(self.score2), True, (100, 200, 50), (200, 100, 400))

    def move(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_w]:
            self.hitbox.y -= self.speed
        if key_list[pygame.K_s]:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 775:
            self.hitbox.bottom = 775
        if self.hitbox.top < 25:
            self.hitbox.top = 25
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = ball.speed
            ball.randomx = randint(1, 6)
            ball.randomy = randint(1, 6)
    def autopilot(self):
        if ball.hitbox.centery < self.hitbox.centery:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 775:
            self.hitbox.bottom = 775
        if self.hitbox.top < 25:
            self.hitbox.top = 25
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed
            ball.randomx = randint(1, 6)
            ball.randomy = randint(1, 6)

class Ball():
    def __init__ (self, x, y, speed):
        self.hitbox = pygame.Rect(x, y, 40, 40)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.randomx = 3
        self.randomy = 3
    def move(self):
        self.hitbox.x += (self.speed_x * self.randomx) / 3
        self.hitbox.y += (self.speed_y * self.randomy) / 3
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.bottom > 800:
            self.speed_y = - self.speed
        if self.hitbox.left < 0:
            player2.score2 += 1
            player2.score2_img = image_generator.render(str(player2.score2), True, (100, 200, 50), (200, 100, 400))
            self.speed_x = self.speed
            self.hitbox.center = (500, 400)
            pygame.time.wait(1000)
        if self.hitbox.right > 1500:
            player1.score1 += 1
            player1.score1_img = image_generator.render(str(player1.score1), True, (100, 200, 50), (200, 100, 400))
            self.hitbox.center = (500, 400)
            self.speed_x = - self.speed


player1 = Player(50, 200, 6)
player2 = Player(1400, 800, 6)
ball = Ball(750, 400, 6)

while True:
    okno.fill((0, 0, 0))
    event_list = pygame.event.get()
    for e in event_list:
        if e.type == pygame.QUIT:
            exit()
    player1.move()
    player2.autopilot()
    ball.move()
    pygame.draw.rect(okno, (255, 0, 0), player1.hitbox)
    pygame.draw.rect(okno, (255, 0, 0), player2.hitbox)
    pygame.draw.rect(okno, (19, 100, 0), ball.hitbox)
    
    okno.blit(player1.score1_img, (100, 50))
    okno.blit(player2.score2_img, (1400, 50))
    pygame.display.update()
    clock.tick(100)