##
#  This program illustrates the steps required to create a bar graph 
#  using the matplotlib module.
#

from matplotlib import pyplot

# Plot data on the graph.
pyplot.bar(1, 1.1)
pyplot.bar(2, 10.0)
pyplot.bar(3, 25.4)
pyplot.bar(4, 44.5)
pyplot.bar(5, 61.0)

# Add descriptive information.
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")

# Display the graph.
pyplot.show()

