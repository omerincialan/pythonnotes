##
#  This program draws a rectangle and vertical line using Python's 
#  turtle graphics package.
#
import turtle

# Draw a square in the default color and pen size.
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# Draw a larger red vertical line to the right of the box.
turtle.pensize(3)
turtle.pencolor("red")
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.pendown()
turtle.forward(100)

# Wait for user input to quit the program.
response = input("Press ENTER to quit.")

