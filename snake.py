from turtle import Turtle
x_positions = [0, -20, - 40]
move_dist = 20
up = 90
down = 270
left = 180
right = 0
starting_positions = ((0, 0), (-20, 0), (-40, 0))


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):

        for position in starting_positions:
            self.add_tail(position)

    def add_tail(self, position):
        tomy = Turtle(shape="square")
        tomy.color("white")
        tomy.penup()
        tomy.goto(position)
        self.turtles.append(tomy)

    def extend(self):
        self.add_tail(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)