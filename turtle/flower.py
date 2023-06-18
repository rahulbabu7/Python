import turtle
t=turtle.Turtle()
t.speed(0)
def flower():
    for i in range(5):
        t.begin_fill()  #! Begin filling the shape
        t.fillcolor("red")  #! Set the fill color to red
        t.circle(190-i,90)
        t.left(90)
        t.circle(190 - i, 90)
        t.left(18)
        t.end_fill() 
flower()
t.hideturtle()
turtle.done()