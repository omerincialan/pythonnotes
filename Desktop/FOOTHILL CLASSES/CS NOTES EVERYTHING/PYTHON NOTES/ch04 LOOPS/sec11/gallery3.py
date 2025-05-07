from ezgraphics import GraphicsWindow, GraphicsImage

GAP = 10

win = GraphicsWindow(750, 350)
canvas = win.canvas()

pic = GraphicsImage("picture1.gif")
canvas.drawImage(0, 0, pic)

pic2 = GraphicsImage("picture2.gif")
x = pic.width() + GAP
canvas.drawImage(x, 0, pic2)

win.wait()

