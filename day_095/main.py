import random
import time
from turtle import Screen
from player import Player
from bullet import Bullet
from enemy import Enemy
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)

screen.bgcolor("black")
screen.title("Space Invaders")

screen.tracer(0)

player = Player()
bullet = Bullet()

scoreboard = Scoreboard()
enemies = []

for _ in range(6):
    enemy = Enemy(random.randint(-350, 350),random.randint(100, 250))
    enemies.append(enemy)

screen.listen()
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")
screen.onkeypress(lambda: bullet.fire(player.xcor(),player.ycor()),"space")

enemy_direction = 3

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.02)
    bullet.move()

    for enemy in enemies:
        enemy.goto(enemy.xcor() + enemy_direction,enemy.ycor())

        if enemy.xcor() > 380 or enemy.xcor() < -380:
            enemy_direction *= -1

            for e in enemies:
                e.goto( e.xcor(),e.ycor() - 30)

        if bullet.distance(enemy) < 20:
            bullet.reset_bullet()
            enemy.goto(random.randint(-350, 350),random.randint(150, 250))
            scoreboard.increase_score()

        if enemy.ycor() < -220:
            game_is_on = False

screen.exitonclick()