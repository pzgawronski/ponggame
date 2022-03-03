from turtle import Turtle
import time

ROUND_COOLDOWN = 0.5
DEFAULT_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.x_move = DEFAULT_SPEED
        self.y_move = DEFAULT_SPEED


    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        time.sleep(ROUND_COOLDOWN)
        self.bounce_x()

    def _speed_up(self, speed):
        return speed + 1 if speed > 0 else speed - 1

    def accelerate(self):
        self.x_move = self._speed_up(self.x_move)
        self.y_move = self._speed_up(self.y_move)

    def _slow_down(self, speed):
        return 10 if speed > 0 else -10

    def reset_speed(self):
        self.x_move = self._slow_down(self.x_move)
        self.y_move = self._slow_down(self.y_move)