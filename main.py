#Importing Libraries
from turtle import Screen, left
from paddle import Paddle
import time
from ball import Ball
# from scoreboard import ScoreBoard

#Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BG_COLOR = 'black'
RIGHT_X_POS = ((SCREEN_WIDTH / 2) - 50)
LEFT_X_POS = - ((SCREEN_WIDTH / 2) - 50)
X_LIMIT = RIGHT_X_POS - 20
Y_LIMIT = (SCREEN_HEIGHT / 2) - 20
MAX_OBJECT_DISTANCE = 50


#Object Setup
window = Screen()
window.bgcolor(BG_COLOR)
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)
window.listen()
window.title('Pong')

right_paddle = Paddle(RIGHT_X_POS, 0)
left_paddle = Paddle(LEFT_X_POS, 0)

# right_scoreboard = ScoreBoard()
# left_scoreboard = ScoreBoard()

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
    if abs(y_ball) >= abs(Y_LIMIT):
        ball.wall_bounce()
    left_object_distance = abs(ball.distance(left_paddle))
    right_object_distance = abs(ball.distance(right_paddle))
    
    if abs(x_ball) >= abs(X_LIMIT) and (left_object_distance < MAX_OBJECT_DISTANCE):
        ball.paddle_bounce()
    elif abs(x_ball) >= abs(X_LIMIT) and (right_object_distance < MAX_OBJECT_DISTANCE):
        ball.paddle_bounce()

window.exitonclick()