from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(-220,250)
        self.write(f"Level {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("black")
        self.hideturtle()
        self.write(f"Game over!", align="center", font=FONT)