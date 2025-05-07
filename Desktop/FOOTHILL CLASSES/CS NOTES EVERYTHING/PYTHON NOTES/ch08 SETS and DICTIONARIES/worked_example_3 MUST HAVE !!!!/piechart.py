##
#  This module defines extensions to the graphics module for drawing
#  a pie chart and a chart legend.
#

## Draws a pie chart on a canvas inside an invisible bounding square.
#  @param x x-coord of the upper-left corner of the bounding square
#  @param y y-coord of the upper-left corner of the bounding square
#  @param diameter the diameter of the bounding square
#  @param slices a list of dictionaries that specify the "size" and
#  "color" of each slice.
#  @param canvas the canvas on which to draw the pie chart
#
def drawPieChart(x, y, diameter, slices, canvas) :
   startAngle = 0
   for piece in slices :
      extent = 360 * piece["size"]
      canvas.setColor(piece["color"])
      canvas.drawArc(x, y, diameter, startAngle, extent)
      startAngle = startAngle + extent
      
## Draws a legend, consisting of a colored box and text, on a canvas.
#  @param x x-coord of the starting position of the entries
#  @param y y-coord of the top position of the first entry
#  @param entries a list of dictionaries that specify the information 
#  for each entry: "color", "label", "size"
#  @param canvas the canvas on which to draw the legend
#
def drawLegend(x, y, entries, canvas) :
   for entry in entries :
      canvas.setColor(entry["color"])
      canvas.drawRect(x, y, 10, 10)
      canvas.setColor("black")
      text = entry["label"] + " (%.1f%%)" % (entry["size"] * 100)
      canvas.drawText(x + 15, y, text)
      y = y + 20      

