import random
from turtle import Turtle
from random import Random
colors = ["red", "yellow", "blue", "pink", "purple"]
PACE = 10
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car = []
        self.speed = 5
        self.level = 1


    def generate_cars(self):
        frequency = random.randint(1,4)
        if frequency == 2:


            cars = Turtle("square")

            cars.penup()
            cars.color(random.choice(colors))
            cars.shapesize(stretch_wid=1,stretch_len=2)
            cars.setheading(180)
            random_y = random.randint(-255, 240)
            cars.goto(310, random_y)
            self.car.append(cars)

    def move_cars(self):
        for i in self.car:
            i.forward(self.speed)

    def reset_cars(self):
        self.hideturtle()
        self.reset()
        self.penup()
        self.car.clear()
        self.generate_cars()
        self.move_cars()

    def level_up(self):
        self.speed += PACE
        self.level += 1



