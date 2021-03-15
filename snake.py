from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:


    def __init__(self):
        self.snake_body = []
        for i in range(3):
            tim = Turtle()
            tim.color("white")
            tim.shape("square")
            tim.penup()
            tim.sety(0)
            tim.turtlesize(1, 1)
            tim.setx(0 - (MOVE_DISTANCE * len(self.snake_body)))
            self.snake_body.append(tim)


    def move_snake(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[seg_num - 1].xcor()
            y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x, y)

        self.snake_body[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)




