import turtle
import os
import winsound

wn_height = 600
wn_width = 800

paddle_pos = ((wn_width/2)-50)

#Initialising window

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=wn_width, height=wn_height)
wn.tracer(0)

#Middle line
m_line = turtle.Turtle()
m_line.speed(0)
m_line.shape("square")
m_line.shapesize(stretch_len=0.2, stretch_wid=(wn_height/2)/10)
m_line.color("white")
m_line.penup()
m_line.goto(0, 0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-paddle_pos, 0)

#Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(paddle_pos, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

#Scores
score_a = 0
score_b = 0


#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




#Game run

while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    #Vertical borders
    if ball.ycor() > (wn_height/2)-10:
        ball.sety((wn_height/2)-10)
        ball.dy *= -1
        # os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -((wn_height/2)-15):
        ball.sety(-((wn_height/2)-15))
        ball.dy *= -1
        # os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Horizontal borders
    if ball.xcor() > (wn_width/2)-10:
       ball.setx(0)
       ball.sety(0)
       score_a+=1
       pen.clear()
       pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

   
    if ball.xcor() < -((wn_width/2)-10):
        ball.setx(0)
        ball.sety(0)
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))


    #Collision check
    if(ball.xcor() < paddle_a.xcor()+10 and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50)):
        ball.setx(paddle_a.xcor()+10)
        ball.dx *= -1
        # os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if(ball.xcor() > paddle_b.xcor()-10 and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50)):
        ball.dx *= -1
        # os.system("aplay bounce.wav&")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)