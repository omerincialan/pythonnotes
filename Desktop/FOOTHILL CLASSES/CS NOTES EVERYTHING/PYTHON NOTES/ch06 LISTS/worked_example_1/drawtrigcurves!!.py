##
# This program creates a line graph containing the curves for the sine and 
# cosine trigonometric functions for x-values between -180 and 180 degrees.
#

from matplotlib import pyplot
from math import pi, sin, cos

# Create empty lists to store the y-values for the sine and cosine curves. 
sinY = []
cosY = []

# The x-values will be the same for both curves.
trigX = []

# Compute the y-values for the sine and cosine curves.
angle = -180
while angle <= 180 :
   x = pi / 180 * angle 
   trigX.append(x)
  
   y = sin(x)
   sinY.append(y)
  
   y = cos(x)
   cosY.append(y)
   angle = angle + 1

# Plot the two curves.
pyplot.plot(trigX, sinY)
pyplot.plot(trigX, cosY)
  
# Add descriptive information.
pyplot.title("Trigonometric Functions")

# Improve the appearance of the graph.
pyplot.legend(["sin(x)", "cos(x)"])
pyplot.grid("on")
pyplot.axis("equal")
pyplot.axhline(color="k")
pyplot.axvline(color="k")

pyplot.show()

