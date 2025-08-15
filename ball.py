from turtle import Turtle
TOP_WALL = 300
BOTTOM_WALL = -300
LEFT_WALL = -400
RIGHT_WALL = 400

class Ball(Turtle):
    """
    Handles all logic with the ball

    Methods:
    -move_ball
    -bounce_y
    -bounce_x
    -reset_ball
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1

    def move_ball(self):
        """Moves the ball at the start of the game"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounces the ball vertically, setting the y to the opposite"""
        self.y_move *= -1


    def bounce_x(self):
        """Bounces the ball horizontally, setting the x to the opposite and increases the speed"""
        self.x_move *= -1
        self.move_speed *= .9
        

    def reset_ball(self):
        """Centers the ball on the screen and resets the speed"""
        self.goto(0,0)
        self.bounce_x()
        self.move_speed(.1)

