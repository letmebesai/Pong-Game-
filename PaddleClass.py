#copying the functons created in the pong game into this class
from turtle import Turtle 

class New_Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
#moving the paddle up and down 
    def paddle_up(self):
     new_y = self.ycor()+15
     self.goto(self.xcor(),new_y)
     


    def paddle_down(self):
        new_y= self.ycor()-15
        self.goto(self.xcor(), new_y)

    
    

