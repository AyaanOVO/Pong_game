from turtle import Turtle
import time
class Ball(Turtle):
    x = 0
    y = 0
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.T = 0.1

    def move_ball(self):
        self.x += self.x_move
        self.y += self.y_move
        self.goto(self.x,self.y)


    def bounce(self):
        self.y_move *= -1

    def down_ball(self):
        self.x_move *= -1

    def left_go(self):
        self.goto(0,0)
        self.x = 0
        self.y = 0
        self.y_move = -10
        self.x_move = -10

    def right_go(self):
        self.goto(0,0)
        self.x = 0
        self.y = 0
        self.y_move = 10
        self.x_move = 10



