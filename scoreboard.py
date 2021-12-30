from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100,250)
        self.write(str(self.score_left), False, 'center', ('Courier',30,'normal'))
        self.goto(100,250)
        self.write(str(self.score_right), False, 'center', ('Courier',30,'normal'))



    def left_increment(self):
        self.score_left += 1
        self.update_scoreboard()

    def right_increment(self):
        self.score_right += 1
        self.update_scoreboard()



