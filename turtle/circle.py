import turtle

radius = 3  # Radius in cm

# Set up the turtle
my_turtle = turtle.Turtle() #!create turtle object
my_turtle.speed(1)  # Set the turtle's speed


my_turtle.begin_fill()  #! Begin filling the shape
my_turtle.fillcolor("red")  #! Set the fill color to red
# Draw the circle
my_turtle.circle(radius * 10)  # Multiply radius by 10 to convert cm to units
my_turtle.end_fill()  #!finish filling the color insode the shape


turtle.done()
