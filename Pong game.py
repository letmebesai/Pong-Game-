# Pong Game with Scoreboard
from turtle import Turtle, Screen
from PaddleClass import New_Paddle
from MyPongBall import PongBall
from time import sleep
from Scorboard import Scoreboard

# Set up the screen
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=800)
my_screen.title("Pong Game")
my_screen.tracer(0)

# Create paddles, ball, and scoreboard
R_paddle = New_Paddle((350, 0))
L_paddle = New_Paddle((-350, 0))
Ball = PongBall()
my_scoreboard = Scoreboard()

# Paddle controls
my_screen.listen()
my_screen.onkey(R_paddle.paddle_down, "Down")
my_screen.onkey(R_paddle.paddle_up, "Up")
my_screen.onkey(L_paddle.paddle_down, "s")
my_screen.onkey(L_paddle.paddle_up, "w")

game_is_on = True
while game_is_on:
    sleep(0.1)
    my_screen.update()
    Ball.move()

    # Bounce off top and bottom walls
    if Ball.ycor() > 350 or Ball.ycor() < -350:
        Ball.bounce_y()

    # Detect collision with right paddle
    if Ball.xcor() > 330 and Ball.distance(R_paddle) < 50 and Ball.ycor() < R_paddle.ycor() + 50 and Ball.ycor() > R_paddle.ycor() - 50:
        Ball.bounce_x()

    # Detect collision with left paddle
    if Ball.xcor() < -330 and Ball.distance(L_paddle) < 50 and Ball.ycor() < L_paddle.ycor() + 50 and Ball.ycor() > L_paddle.ycor() - 50:
        Ball.bounce_x()

    # Detect if ball goes out of bounds (right side) - Left player scores
    if Ball.xcor() > 380:
        Ball.goto(0, 0)
        Ball.bounce_x()
        my_scoreboard.l_point()  # Increment left player's score and update scoreboard

    # Detect if ball goes out of bounds (left side) - Right player scores
    if Ball.xcor() < -380:
        Ball.goto(0, 0)
        Ball.bounce_x()
        my_scoreboard.r_point()  # Increment right player's score and update scoreboard

my_screen.exitonclick()
