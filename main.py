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

from turtle import Screen
from paddle import Paddle

game_area = Screen()
game_area.title("Pong")
game_area.setup(width=800, height=600)
game_area.bgcolor("black")
game_area.tracer(0)
game_area.listen()

player_paddle = Paddle("RIGHT")
computer_paddle = Paddle("LEFT")
game_area.onkey(player_paddle.move_up, "Up")
game_area.onkey(player_paddle.move_down, "Down")

game_on = True
while game_on:
    game_area.update()

game_area.update()
game_area.exitonclick()
