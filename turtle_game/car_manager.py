
from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
car_speed = 5
class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(colors))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)
    
    def move(self):
        for car in self.cars:
            car.backward(car_speed)
    def all_cars(self):
        return self.cars
    
    def clear_cars(self):
        for car in self.cars:
            car.hideturtle()
            car.clear()
        self.cars = []
    
    def level_up(self):
        global car_speed
        car_speed += 5
        self.clear_cars()
        self.create_car()
