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
car_manager = CarManager()

#sterowanie
screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')

FINISH_LINE_Y = 280

TIME = 0.1

game_is_on = True
while game_is_on:
    time.sleep(TIME)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detecting collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    #if turtle reach top, increase level and reset
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        #increasing speed of game
        TIME *= 0.9



screen.exitonclick()