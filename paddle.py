from turtle import Turtle

PACE = 20
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_X = {
    "RIGHT": 350,
    "LEFT": -350
}
PADDLE_Y = 0
UP = 20
DOWN = -20


class Paddle(Turtle):

    def __init__(self, screen_side):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(PADDLE_X[screen_side], PADDLE_Y)
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)

    def _move(self, direction):
        self.goto(self.xcor(), self.ycor() + direction)

    def move_up(self):
        self._move(UP)

    def move_down(self):
        self._move(DOWN)
