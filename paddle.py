from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    Handles all logic with user controlled paddles

    Methods:
    -up
    -down
    """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        """Moves the paddle up"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves paddle down"""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)