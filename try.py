import turtle

wn = turtle.Screen()
wn.setup(width=200,height=200)
wn.tracer(0)

# a = turtle.Turtle()
# a.shape("square")
# a.goto(0, 0)


b = turtle.Turtle()
b.shape("square")
b.goto(10, 10)


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("ABCD", font=("Courier", 20, "normal"))



while True:
    wn.update()
