from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen =  Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # Detect Collision

    if snake.snake_body[0].distance(food)<15:
        food.update_loc()
        snake.extend()
        score.score +=1
        score.print_score()

    # Detect Collision with wall
    if snake.snake_body[0].xcor()>280 or snake.snake_body[0].xcor()<-280 or snake.snake_body[0].ycor()>300 or snake.snake_body[0].ycor()<-300:
        game_on = False
        score.game_over()

    # Detect Collision with tail
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            game_on = False
            score.game_over()



screen.exitonclick()