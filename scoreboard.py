from turtle import Turtle

class Scoreboard(Turtle):
    """
    All logic for the scoreboard

    Methods:
    -update_scoreboard
    -left_point
    -right_point
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
       

    def update_scoreboard(self):
        """Creates the scoreboard, clears it, and displays it"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font= ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font= ("Courier", 80, "normal"))

    def left_point(self):
        """Adds a point to the left and updates the board"""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Adds a point to the right and updates the board"""
        self.right_score += 1
        self.update_scoreboard()
