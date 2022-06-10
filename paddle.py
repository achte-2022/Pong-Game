# Importing Libraries
from turtle import Turtle

# Constants
SHAPE = "square"
COLOR = "white"
HEIGHT_FACTOR = 5
WIDTH_FACTOR = 1
SPEED = "fastest"
UP = 90
DOWN = 270
FORWARD_DISTANCE = 30

# Paddle Class
class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_len=HEIGHT_FACTOR, stretch_wid=WIDTH_FACTOR)
        self.speed(SPEED)
        self.goto(x_pos, y_pos)
        self.setheading(UP)
        return

    def up(self):
        if self.heading() == UP:
            self.forward(FORWARD_DISTANCE)
            return
        else:
            self.setheading(UP)
            self.forward(FORWARD_DISTANCE)
            return

    def down(self):
        if self.heading() == DOWN:
            self.forward(FORWARD_DISTANCE)
            return
        else:
            self.setheading(DOWN)
            self.forward(FORWARD_DISTANCE)
            return
