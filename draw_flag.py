import turtle

# Set up the turtle window
turtle.setup(width=600, height=400)
turtle.bgcolor("white")

# Define the flag dimensions
width = 300
height = 200
def draw_german_flag():
    # Draw the black stripe
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height/3)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()

    # Draw the red stripe
    turtle.penup()
    turtle.goto(-width/2, height/6)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    turtle.left(90)
    turtle.forward(height/3)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height/3)

    turtle.end_fill()

    # Draw the yellow stripe
    turtle.penup()
    turtle.goto(-width/2, -height/6)
    turtle.pendown()
    turtle.color("gold")
    turtle.begin_fill()
    turtle.forward(-height/3)
    turtle.right(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height/3)
    turtle.end_fill()

    # Hide the turtle cursor
    turtle.hideturtle()

    # Exit on click
    turtle.exitonclick()
    
draw_german_flag()
