#Importing Libraries
from turtle import Turtle

#Constants
SHAPE = 'circle'
SPEED = 'fastest'
COLOR = 'white'
X_INIT = 0
Y_INIT = 0
WIDTH_FACTOR = 1
HEIGHT_FACTOR = 1
INIT_ANGLE = 90 + 30


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
        return
    
    def move(self):
        # self.settiltangle(45)
        self.forward(10)

    def wall_bounce(self):
        self.setheading(360 - self.heading())
        return

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
        return
