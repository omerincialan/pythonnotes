from ezgraphics import GraphicsWindow, GraphicsImage

GAP = 10
NUM_PICTURES = 20

win = GraphicsWindow(750, 350)
canvas = win.canvas()

pic = GraphicsImage("picture1.gif")
canvas.drawImage(0, 0, pic)

x = 0
for i in range(2, NUM_PICTURES + 1) :
   previous = pic
   filename = "picture%d.gif" % i
   pic = GraphicsImage(filename)
   x = x + previous.width() + GAP
   canvas.drawImage(x, 0, pic)

win.wait()

