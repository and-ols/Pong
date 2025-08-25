# Pong

## Overview
This version of pong was built using the built in Turtle graphics module, documentation for this can be found below. The game consists of two paddles (created from the same class), and a ball. At the start of the game the paddles are centered and placed on the left and right and the ball in the middle. The ball then moves to the top left of the screen and the players control the movement via w, s up arrow and the down arrow keys. When a player misses a ball, the other player is awarded a point. The more time the ball bounces the faster the balls speed moves. Game over is achieved when the program is closed.

## Files
- **main**: The role of the main file is to hold all the logic for the game. Main handles the checking if the ball has hit a wall, the detection of a hit paddle, a point scored and reset, calling all of these from their respective classes. Main also handles the set-up of the screen, adn the keys used to move the paddles.

- **paddle**: The paddle file holds the paddle class. This  is where all logic for the paddle is stored with creation, and up and down movement.

- **ball**: This holds the ball class. The ball creates a ball on the screen and handles the logic for bouncing the ball and speeding the ball up after each bounce. It also handles the reset of the ball to its central position, reversing the last angle it was moving towards.

- **scoreboard**: The scoreboard holds the scoreboard class and handles the display of each of the players current score.

# Demos
### Start of game
![Start of game demo](<Pong demo - Trim2.mkv.gif>)
### Game continuing, speeding up
![Game speeding up](<Pong demo - Trim.mkv.gif>)

## Documentation
- [Turtle Graphics](https://docs.python.org/3/library/turtle.html)