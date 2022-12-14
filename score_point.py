from turtle import Turtle
class Firstplayer(Turtle):
    score1 = 0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-100,200)
        self.write(self.score1, align="center", font=("Courier", 50 , "bold"))

    def score_of_1(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.score1, align="center", font=("Courier", 50 , "bold"))