from turtle import Turtle, Screen
import random
from paddle import Paddle

# 1. create screen
# 2. create and move the paddle
# 3. create another paddle
# 4. create the ball and make it move
# 5. detect collision with wall and make it bounce back randomly
# 6. detect collision with user paddle and make it bounce back
# 7. detect when paddle misses the ball
# 8. keep score on scoreboard visible to user(s)


# creating screen
screen = Screen()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()

# establishing event listeners so paddle can be controlled





screen.exitonclick()