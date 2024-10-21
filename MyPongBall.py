#creating the  ball for pong game 
from turtle import Turtle

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        
        self.x_move = 18  # X-axis movement speed
        self.y_move = 18  # Y-axis movement speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move*=-1
        
    def bounce_x(self):
        self.x_move*=-1
