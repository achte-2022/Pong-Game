# Importing Libraries
from turtle import Turtle

# Constants
SHAPE = "circle"
SPEED = "fastest"
COLOR = "white"
X_INIT = 0
Y_INIT = 0
WIDTH_FACTOR = 1
HEIGHT_FACTOR = 1
INIT_ANGLE = 45


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.speed(SPEED)
        self.shapesize(stretch_len=HEIGHT_FACTOR, stretch_wid=WIDTH_FACTOR)
        self.goto(X_INIT, Y_INIT)
        self.setheading(INIT_ANGLE)
        self.right_init_angle = INIT_ANGLE
        self.left_init_angle = 180 + INIT_ANGLE
        self.forward_steps = 10
        return

    def move(self):
        self.forward(self.forward_steps)

    def wall_bounce(self):
        self.setheading(360 - self.heading())
        self.forward_steps += 2
        return

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
        self.forward_steps += 2
        return
