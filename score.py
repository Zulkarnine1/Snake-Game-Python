from turtle import Turtle

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0,250)
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=("Arial",16,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 16, "normal"))


