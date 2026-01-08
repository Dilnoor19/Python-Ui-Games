from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Feed the snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Collision with wall
    if (
        snake.head.xcor() > 280 or 
        snake.head.xcor() < -280 or 
        snake.head.ycor() > 280 or 
        snake.head.ycor() < -280
    ):
        game_on = False
        score.goto(0, 0)
        score.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    # Tail collision
    for segment in snake.segments[1:]:  
        if snake.head.distance(segment) < 10:
            game_on = False
            snake.hide_snake()         
            score.goto(0, 0)
            score.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

            break

screen.exitonclick()
