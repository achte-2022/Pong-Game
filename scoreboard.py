from turtle import Turtle

# Constants
COLOR = "white"
ALIGN = "center"
FONT = ("Courier", 30, "normal")
X_INIT = 70
Y_INIT = 250


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.draw_scoreboard()
        return

    def draw_scoreboard(self):
        self.goto(-X_INIT, Y_INIT)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(X_INIT, Y_INIT)
        self.write(self.right_score, align=ALIGN, font=FONT)
        return

    def left_score_update(self):
        self.left_score += 1
        self.clear()
        self.draw_scoreboard()
        return

    def right_score_update(self):
        self.right_score += 1
        self.clear()
        self.draw_scoreboard()
        return
