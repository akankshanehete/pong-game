from turtle import Turtle

class Ball (Turtle):
     def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0,0)

     def move_top_right_corner(self):
        self.speed("slow")
        self.goto(360,260)
