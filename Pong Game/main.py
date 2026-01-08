from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Global variables to track game objects
r_paddle = None
l_paddle = None
ball = None
scoreboard = None

def start_game():
    global r_paddle, l_paddle, ball, scoreboard

    # Clear old objects if they exist
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("Pong Game")

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    scoreboard.draw_center_line()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce_y()

        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        if ball.xcor() > 380:
            scoreboard.left_point()
            ball.reset_position()

        if ball.xcor() < -380:
            scoreboard.right_point()
            ball.reset_position()

        if scoreboard.l_score == 3 or scoreboard.r_score == 3:
            winner_text = "LEFT PLAYER WINS!" if scoreboard.l_score == 3 else "RIGHT PLAYER WINS!"
            ball.hideturtle()
            scoreboard.game_over(f"{winner_text}")
            game_is_on = False

    screen.onkey(replay_game, "r")
    screen.mainloop()


def replay_game():
    start_game()


start_game()
