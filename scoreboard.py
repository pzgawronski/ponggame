from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def _write_score_1(self):
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Comic Sans MS", 60, "normal"))

    def _write_score_2(self):
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Comic Sans MS", 60, "normal"))

    def p1_point(self):
        self.p1_score += 1

    def p2_point(self):
        self.p2_score += 1

    def update_scoreboard(self):
        self.clear()
        self._write_score_1()
        self._write_score_2()
