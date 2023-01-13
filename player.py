from turtle import Turtle

import car_manager

STARTING_POINT = (0,-280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.reset_game()

    def move(self):

        new_y_coordinate= self.ycor() + 10
        self.goto(self.xcor(), new_y_coordinate)

    def reset_game(self):

        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(STARTING_POINT)



