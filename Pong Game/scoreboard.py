from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        self.l_score += 1
        self.update_score()

    def right_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self, message):
        self.goto(0, 20)
        self.color("red")
        self.write(message, align="center", font=("Courier", 25, "bold"))
        self.goto(0, -40)
        self.write("Press 'R' to Replay", align="center", font=("Courier", 20, "normal"))

    # ------------ DRAW CENTER DOTTED LINE ------------
    def draw_center_line(self):
        line = Turtle()
        line.color("white")
        line.hideturtle()
        line.penup()
        line.goto(0, 300)
        line.setheading(270)  # downward

        for _ in range(30):  # 30 dashes
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(10)
