from turtle import Screen, Turtle
from defender import Defender
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PingPong")
screen.tracer(0)

r_defender = Defender((350, 0))
l_defender = Defender((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_defender.go_up, "Up")
screen.onkey(r_defender.go_down, "Down")

screen.onkey(l_defender.go_up, "w")
screen.onkey(l_defender.go_down, "s")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right defender
    if ball.distance(r_defender) < 50 and ball.xcor() > 320 or ball.distance(l_defender) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when right defender misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when left defender misses   
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
