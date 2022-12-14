from turtle import Turtle,Screen
TURTLE_LOCATION = [(350,40),(350,20),(350,0),(350,-20),(350,-40)]
class Placing1:
    def __init__(self):
        self.list_turtle = []
        self.creating_paddle()

    def creating_paddle(self):
        for i in range(5):
            mypet = Turtle()
            mypet.shape("square")
            mypet.penup()
            mypet.speed(0)
            mypet.color("white")
            mypet.goto(TURTLE_LOCATION[i])
            self.list_turtle.append(mypet)

    def up(self):
        if (self.list_turtle[0].ycor() < 270):
            for i in range(len(self.list_turtle)):
                self.list_turtle[i].setheading(90)
                self.list_turtle[i].forward(20)


    def down(self):
        if (self.list_turtle[-1].ycor() > -270):
            for i in range(len(self.list_turtle)):
                self.list_turtle[i].setheading(270)
                self.list_turtle[i].forward(20)

