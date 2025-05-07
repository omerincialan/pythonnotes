##
#  This program draws two Italian flags using the geometric shape classes. 
#

from ezgraphics import GraphicsWindow
from shapes import Rectangle, Line, Group

# Define constants for the flag size.
FLAG_WIDTH = 150
FLAG_HEIGHT = FLAG_WIDTH * 2 // 3
PART_WIDTH = FLAG_WIDTH // 3

# Create the graphics window.
win = GraphicsWindow(300, 300)
canvas = win.canvas()

# Build the flag as a group shape.
flag = Group()

part = Rectangle(0, 0, PART_WIDTH, FLAG_HEIGHT)
part.setColor("green")
flag.add(part)

part = Rectangle(PART_WIDTH * 2, 0, PART_WIDTH, FLAG_HEIGHT)
part.setColor("red")
flag.add(part)

flag.add(Line(PART_WIDTH, 0, PART_WIDTH * 2, 0))
flag.add(Line(PART_WIDTH, FLAG_HEIGHT, PART_WIDTH * 2, FLAG_HEIGHT))

# Draw the first flag in the upper-left area of the canvas.
flag.moveBy(10, 10)
flag.draw(canvas)

# Draw the second flag in the bottom-right area of the canvas.
flag.moveBy(130, 180)
flag.draw(canvas)

win.wait()

