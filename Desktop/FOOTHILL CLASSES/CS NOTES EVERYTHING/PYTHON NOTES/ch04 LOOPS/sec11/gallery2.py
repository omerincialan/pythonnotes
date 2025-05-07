from ezgraphics import GraphicsWindow, GraphicsImage

win = GraphicsWindow(750, 350)
canvas = win.canvas()

pic = GraphicsImage("picture1.gif")
canvas.drawImage(0, 0, pic)

pic2 = GraphicsImage("picture2.gif")
x = pic.width()
canvas.drawImage(x, 0, pic2)

win.wait()

