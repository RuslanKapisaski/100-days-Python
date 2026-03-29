from turtle import Screen
import time

from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

def handle_events():
    player.move_up()
    scoreboard.increase_score()


screen.onkey(key='Up',fun=handle_events)

screen_time = 0.1

game_is_on = True
while game_is_on:
    time.sleep(screen_time)
    screen.update()
    car_manager.generate_cars()
    car_manager.move_cars()

    # Detect collision
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()





