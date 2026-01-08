from turtle import Turtle

starting_position = [(0,0), (-20,0), (-40,0)]
move_distance = 15


up = 90
Down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        # Add a new segment to the last segment's position
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(move_distance)
    def hide_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
