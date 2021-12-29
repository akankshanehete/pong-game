from turtle import Turtle

# paddle specifications
# width = 20, height = 100
# x_pos = 350
# y_pos = 0
# up or down moves paddle by 20 px respectively


class Paddle (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.goto(350, 0)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)
