from turtle import Turtle

class Border:
    def __init__(self):
        bor = Turtle()
        bor.color("red")
        bor.penup()
        bor.backward(220)
        bor.pendown()
        bor.left(90)
        bor.forward(220)
        bor.right(90)
        bor.forward(440)
        bor.right(90)
        bor.forward(440)
        bor.right(90)
        bor.forward(440)
        bor.right(90)
        bor.forward(240)
        bor.hideturtle()