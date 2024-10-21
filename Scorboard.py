from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the previous score and update the current score display."""
        self.clear()  # Clear the previous score before updating
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        """Increase the left player's score and update the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase the right player's score and update the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
