#Importing Libraries
from turtle import Screen
from paddle import Paddle
import time

#Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BG_COLOR = 'black'
RIGHT_X_POS = ((SCREEN_WIDTH / 2) - 50)
LEFT_X_POS = - ((SCREEN_WIDTH / 2) - 50)

#Object Setup
window = Screen()
window.bgcolor(BG_COLOR)
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)
window.listen()
window.title('Pong')

right_paddle = Paddle(RIGHT_X_POS, 0)
left_paddle = Paddle(LEFT_X_POS, 0)

window.update()

window.onkey(right_paddle.up, "Up")
window.onkey(right_paddle.down, "Down")

window.onkey(left_paddle.up, "w")
window.onkey(left_paddle.down, "s")

is_game_on = True

while is_game_on:
    window.update()
    time.sleep(0.05)








window.exitonclick()