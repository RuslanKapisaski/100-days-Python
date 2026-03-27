from turtle import Turtle

MOVE_DISTANCE = 20
DOWN = 270
LEFT = 180
UP = 90
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        last_segment = self.segments[-1]
        self.add_segment(last_segment.position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
