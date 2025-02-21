from turtle import Turtle

start_position = (0, -280)
move_distance = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(start_position)
        self.setheading(90)
    def move(self):
        self.forward(move_distance)
    
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
        
    def go_to_start(self):
        self.goto(start_position)