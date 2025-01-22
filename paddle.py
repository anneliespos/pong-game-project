from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def up(self):
        """Move paddle up"""
        new_y= self.ycor() +20
        if new_y <280:
            self.goto(self.xcor(), new_y)

    def down(self):
        """Move paddle down"""
        new_y = self.ycor() - 20
        if new_y > -280:
            self.goto(self.xcor(), new_y)


