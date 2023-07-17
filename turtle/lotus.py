#!print lotus

import turtle

flower = turtle.Turtle()

for i in range(5):
    flower.circle(190-i,90)
    flower.left(90)
    flower.circle(190-i,90)
    flower.left(60)
turtle.done()