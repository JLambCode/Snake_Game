import turtle
from turtle import Turtle
import random


turtle.colormode(255)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed("fastest")
        self.color(random.randint(25, 255), random.randint(25, 255), random.randint(25, 255))
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.color(random.randint(25, 255), random.randint(25, 255), random.randint(25, 255))
        self.goto(random_x, random_y)

