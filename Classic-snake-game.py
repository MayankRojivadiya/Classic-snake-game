from turtle import Screen
import time
from src.snake import Snake
from src.food import Food
from src.score import Score
from src.border import Border

screen = Screen()
screen.setup(width=700, height=620)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
border = Border()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        snake.extend()
        score.increase_score()  

    if snake.head.xcor() > 210 or snake.head.xcor() < -210 or snake.head.ycor() > 210 or snake.head.ycor() < -210:
        score.reset_scr()
        snake.reset_snake()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score.reset_scr()
            snake.reset_snake()

screen.exitonclick()