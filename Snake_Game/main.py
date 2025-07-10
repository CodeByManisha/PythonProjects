from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard




screen = Screen()
mit = Turtle()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect Collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail
    #if head collides with any segment of the tail then trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

























screen.exitonclick()