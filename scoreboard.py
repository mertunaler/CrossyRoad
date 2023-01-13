from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.reset_scoreboard()


    def reset_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(-170, 275)
        self.write(arg=f"Level:{self.level}", align="left", font=("Comic Sans MS", 15, "bold"))


    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=("Comic Sans MS", 25, "bold"))

