from turtle import Turtle, Screen
import random
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
screen.tracer(0)

# creating 2 paddles that can be moved by the user
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)

# creating the ball
ball = Ball()
sb = Scoreboard()
screen.update()

# establishing event listeners so paddle can be controlled
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290 :
        ball.bounce()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 330 or ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    # detect missed ball by right player; left player gets a point
    if ball.xcor() >= 380:
        sb.left_increment()
        ball.refresh()

    # detect missed ball by left player; right player gets a point
    if ball.xcor() <= -380:
        sb.right_increment()
        ball.refresh()

       # game_is_on = False



screen.exitonclick()