from turtle import Turtle
import time

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        # new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
            self.move()
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
            self.move()
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
            self.move()
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
            self.move()