from turtle import Turtle,Screen,bgcolor
from paddles import Placing1
from paddles2 import Placing2
from pong_ball import Ball
from score_point2 import Secondplayer
from score_point import Firstplayer
import time
BG = bgcolor("black")
screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")

screen.tracer(0)

ob_placing = Placing1()
ob_placing2 = Placing2()
ob_score1 = Firstplayer()
ob_score2 = Secondplayer()
ball_game = Ball()

tim = Turtle()
tim.color("white")
tim.penup()
tim.goto(0,-280)
tim.pensize(5)
tim.setheading(90)
for i in range(100):
    tim.pendown()
    tim.forward(30)
    tim.penup()
    tim.forward(30)

screen.update()
screen.tracer(0)

screen.listen()
screen.onkey(fun=ob_placing.up,key="Up")
screen.onkey(fun=ob_placing.down,key="Down")
screen.onkey(fun=ob_placing2.upper,key="w")
screen.onkey(fun=ob_placing2.downer,key="s")

flag = True
G = 0

pos1 = ob_placing.list_turtle
i = 0
pos2 = ob_placing2.turtle_list2
while flag:
    screen.update()
    time.sleep(ball_game.T)
    ball_game.move_ball()

    if(ball_game.ycor() > 280 or ball_game.ycor() < -280):
        ball_game.bounce()


    if (pos1[G].distance(ball_game) < 30 or pos2[G].distance(ball_game) < 30):
        ball_game.down_ball()
        ball_game.T *= 0.9


    if (pos1[G+2].distance(ball_game) < 30 or pos2[G+2].distance(ball_game) < 30):
        ball_game.down_ball()
        ball_game.T *= 0.9


    if (pos1[G+4].distance(ball_game) < 30 or pos2[G+4].distance(ball_game) < 30):
        ball_game.down_ball()
        ball_game.T *= 0.9

    if (pos1[G].xcor() + 36 < ball_game.xcor()):
        ob_score1.score1 += 1
        ob_score1.score_of_1()
        ball_game.T = 0.1
        ball_game.left_go()

    if (pos2[G].xcor()  > ball_game.xcor()+36):
        ob_score2.score2 += 1
        ob_score2.score_of_2()
        ball_game.T = 0.1
        ball_game.right_go()





screen.exitonclick()