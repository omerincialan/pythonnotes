##
#  This program reads a stock portfolio from a text file and produces a
#  graphical pie chart of the stock allocations by category.
#

from ezgraphics import GraphicsWindow
from piechart import drawPieChart, drawLegend
from portfolio import loadAllocations, buildChartData

PIE_SIZE = 150

# Load the stock allocations and compute the percentages.
allocations = loadAllocations("stocks.txt")
slices = buildChartData(allocations)

# Create the graphics window and draw the pie chart and legend.
height = PIE_SIZE + 75 + len(slices) * 20

win = GraphicsWindow(PIE_SIZE + 100, height)
canvas = win.canvas()
drawPieChart(50, 25, PIE_SIZE, slices, canvas)
drawLegend(50, PIE_SIZE + 50, slices, canvas)
win.wait()   

