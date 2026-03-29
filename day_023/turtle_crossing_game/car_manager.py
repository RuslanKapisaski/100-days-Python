from turtle import Turtle
from random import choice, randint

CAR_COLORS = ['red', 'green', 'blue', 'yellow', 'pink']
MOVE_SPEED = 5
STARTING_MOVE_DISTANCE = 5
STARTING_X_COORDINATES = 300


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_SPEED

    def generate_cars(self):
        chance = randint(0,6)
        if chance == 1:
            self.new_car = Turtle("square")
            self.new_car.shapesize(stretch_wid=1,stretch_len=2)
            self.new_car.color(choice(CAR_COLORS))
            self.new_car.penup()
            random_y = randint(-250,250)
            self.new_car.goto(x=STARTING_X_COORDINATES,y=random_y)
            self.all_cars.append(self.new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def detect_collision(self, obj):
        for car in self.all_cars:
            if car.distance(obj) < 20:
                return True

    def level_up(self):
        self.car_speed += MOVE_SPEED


