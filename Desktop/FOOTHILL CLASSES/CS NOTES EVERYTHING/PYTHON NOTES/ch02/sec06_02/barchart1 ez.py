##
#  This program draws three rectangles on a canvas.
#

from ezgraphics import GraphicsWindow

# Create the window and access the canvas.
win = GraphicsWindow(400, 200)
canvas = win.canvas()

# Draw on the canvas.
canvas.drawRect(0, 10, 200, 10)
canvas.drawRect(0, 30, 300, 10)
canvas.drawRect(0, 50, 100, 10)

# Wait for the user to close the window.
win.wait()

