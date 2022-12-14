from turtle import Turtle,Screen
PADDLE2_LOCATION = [(-350,40),(-350,20),(-350,0),(-350,-20),(-350,-40)]
class Placing2:
    def __init__(self):
        self.turtle_list2 = []
        self.creating_paddle2()

    def creating_paddle2(self):
        for i in range(5):
            mypet = Turtle()
            mypet.shape("square")
            mypet.penup()
            mypet.color("white")
            mypet.goto(PADDLE2_LOCATION[i])
            self.turtle_list2.append(mypet)

    def upper(self):
        if (self.turtle_list2[0].ycor() < 270):
            for i in range(len(self.turtle_list2)):
                self.turtle_list2[i].setheading(90)
                self.turtle_list2[i].forward(20)

    def downer(self):
        if (self.turtle_list2[-1].ycor() > -270):
            for i in range(len(self.turtle_list2)):
                self.turtle_list2[i].setheading(270)
                self.turtle_list2[i].forward(20)

