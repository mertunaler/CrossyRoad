import time
import turtle
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import ScoreBoard

STARTING_SPEED = 0.1

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("gray")

screen.update()


screen.listen()

player = Player()
car = Car()
scoreboard = ScoreBoard()

screen.onkeypress(player.move, "w")

is_game_on = True

while is_game_on:

    time.sleep(0.1)

    car.generate_cars()
    car.move_cars()

    screen.update()

    for i in car.car:
        if i.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    if player.ycor() > 250:
        screen.reset()
        scoreboard.level += 1
        player.reset_game()
        car.reset_cars()
        car.level_up()
        scoreboard.reset_scoreboard()

screen.exitonclick()
