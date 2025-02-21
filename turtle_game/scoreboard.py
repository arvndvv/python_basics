from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=("Arial", 24, "normal"))
    
    def update_level(self):
        self.clear()
        self.level += 1
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
      