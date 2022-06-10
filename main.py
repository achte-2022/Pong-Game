# Importing Libraries
from turtle import Screen
import turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard

# Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BG_COLOR = "black"
RIGHT_X_POS = (SCREEN_WIDTH / 2) - 50
LEFT_X_POS = -((SCREEN_WIDTH / 2) - 50)
X_LIMIT = RIGHT_X_POS - 20
Y_LIMIT = (SCREEN_HEIGHT / 2) - 20
MAX_OBJECT_DISTANCE = 50
X_INIT = 0
Y_INIT = 0
MAX_SCORE = 11
ALIGN = "left"
FONT = ("Arial", 12, "normal")


# Object Setup
window = Screen()
window.bgcolor(BG_COLOR)
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)
window.listen()
window.title("Pong")

right_paddle = Paddle(RIGHT_X_POS, X_INIT)
left_paddle = Paddle(LEFT_X_POS, Y_INIT)

scoreboard = ScoreBoard()

ball = Ball()
window.update()

window.onkey(right_paddle.up, "Up")
window.onkey(right_paddle.down, "Down")

window.onkey(left_paddle.up, "w")
window.onkey(left_paddle.down, "s")

is_game_on = True

while is_game_on:
    ball.move()
    window.update()
    time.sleep(0.05)
    y_ball = ball.ycor()
    x_ball = ball.xcor()
    if abs(y_ball) > abs(Y_LIMIT):
        ball.wall_bounce()
    left_object_distance = abs(ball.distance(left_paddle))
    right_object_distance = abs(ball.distance(right_paddle))
    if (x_ball > X_LIMIT) and (right_object_distance >= MAX_OBJECT_DISTANCE):
        scoreboard.left_score_update()
        ball.goto(X_INIT, Y_INIT)
        window.update()
        ball.setheading(ball.left_init_angle)
        time.sleep(1)
        ball.forward_steps = 10
    elif (x_ball < -X_LIMIT) and (left_object_distance >= MAX_OBJECT_DISTANCE):
        scoreboard.right_score_update()
        ball.goto(X_INIT, Y_INIT)
        window.update()
        ball.setheading(ball.right_init_angle)
        time.sleep(1)
        ball.forward_steps = 10
    elif abs(x_ball) > abs(X_LIMIT) and (left_object_distance < MAX_OBJECT_DISTANCE):
        ball.paddle_bounce()
    elif abs(x_ball) > abs(X_LIMIT) and (right_object_distance < MAX_OBJECT_DISTANCE):
        ball.paddle_bounce()

    if scoreboard.left_score >= MAX_SCORE:
        is_game_on = False
        window.clear()
        turtle.penup()
        turtle.goto(-100, 0)
        turtle.write(
            f"Left Player has won. Score: {scoreboard.left_score}-{scoreboard.right_score}",
            align=ALIGN,
            font=FONT,
        )
        turtle.hideturtle()
        window.update()

    elif scoreboard.right_score >= MAX_SCORE:
        is_game_on = False
        window.clear()
        turtle.penup()
        turtle.goto(-100, 0)
        turtle.write(
            f"Right Player has won. Score: {scoreboard.left_score}-{scoreboard.right_score}",
            align=ALIGN,
            font=FONT,
        )
        turtle.hideturtle()
        window.update()
window.exitonclick()
