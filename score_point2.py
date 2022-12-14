from turtle import Turtle
class Secondplayer(Turtle):
    score2 = 0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(100,200)
        self.write(self.score2, align="center", font=("Courier", 50 , "bold"))

    def score_of_2(self):
        self.clear()
        self.goto(100,200)
        self.write(self.score2, align="center", font=("Courier", 50, "bold"))