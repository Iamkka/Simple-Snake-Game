from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(600,600)
screen.bgcolor('black')
screen.tracer(0)


# Buat object snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

end_game = False
while not end_game:   
    screen.update() 
    time.sleep(0.1)

    snake.move()

    if snake.head.xcor() >= 300 or snake.head.xcor() <=-300:
        end_game = True

    if snake.head.ycor() >= 300 or snake.head.ycor() <=-300:
        end_game = True 

    if snake.head.distance(food) < 15:
        #kepala ular mengenai makanannya

        #buat makanan pindah acak
        food.move_random()
        snake.extend()
        scoreboard.add_score()

    for s in snake.snakes:
        if s == snake.head:
            continue
        if snake.head.distance(s) < 15:
            end_game = True

    
screen.exitonclick()