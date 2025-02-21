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