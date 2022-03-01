from turtle import Turtle

PACE_X = 20
PACE_Y = 15

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)

    def move(self):
        self.goto(self.xcor()+PACE_X, self.ycor()+PACE_Y)

