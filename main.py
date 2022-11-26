from turtle import Screen, Turtle
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()


#sterowanie
screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')

FINISH_LINE_Y = 280

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #if turtle reach top, increase level and reset
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()