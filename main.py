from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creates and sets the paddles, ball and scoreboard
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Detects the arrow keys being pressed
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_over = False
while not game_over:
    screen.update()
    time.sleep(ball.move_speed)

    # Starts the balls movement
    ball.move_ball()

    # Check wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check paddle collision
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Right paddle miss
    if ball.xcor() > 380: 
        ball.reset_ball()
        scoreboard.left_point()
    # Left paddle miss
    elif ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_point()



screen.exitonclick()