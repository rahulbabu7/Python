import turtle

# Set up the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(1)  # Set the turtle's speed

# Draw the star with 6 points
for _ in range(5):
    my_turtle.forward(100)  # Move forward
    my_turtle.left(144)  # Turn right by 144 degrees

turtle.done()


