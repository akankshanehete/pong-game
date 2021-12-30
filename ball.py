from turtle import Turtle
import time

class Ball (Turtle):
     def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.x_move = 2
        self.y_move = 2

     def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

     # changing ball y direction
     def bounce(self):
        self.y_move *= -1

     # detect collision with paddle
     def paddle_bounce(self):
        self.x_move *= -1.01

     def refresh(self):
        time.sleep(1)
        self.goto(0,0)
        self.x_move *= -1
        self.move()



