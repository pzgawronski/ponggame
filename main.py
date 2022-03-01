# TODO 1: Initialize screen
# TODO 1.1: Make a dashed line across the middle
# TODO 2: Establish pallet class
# TODO 2.1: Make pallet react to keyboard strokes
# TODO 2.2: Make computer pallet move on its own
# TODO 3: Establish scoreboard class
# TODO 4: Establish ball class
# TODO 5.1: Implement collision detection between ball and pallets
# TODO 5.2: Implement collision detection between ball game area border
# TODO 6: Implement scoring
# TODO 6.1: Implement game over on score 10
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

game_area = Screen()
game_area.title("Pong")
game_area.setup(width=800, height=600)
game_area.bgcolor("black")
game_area.tracer(0)
game_area.listen()

player1_paddle = Paddle("LEFT")
player2_paddle = Paddle("RIGHT")
game_area.onkey(player1_paddle.move_up, "w")
game_area.onkey(player1_paddle.move_down, "s")
game_area.onkey(player2_paddle.move_up, "Up")
game_area.onkey(player2_paddle.move_down, "Down")
ball = Ball()

game_on = True
while game_on:
    game_area.update()
    time.sleep(0.05)
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(player2_paddle) < 50 and ball.xcor() > 320) \
            or (ball.distance(player1_paddle) < 50 and ball.xcor() < -320):
        # Bounce
        ball.bounce_x()

game_area.exitonclick()
