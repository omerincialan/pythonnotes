##
#  This program creates a bar graph that illustrates the 
#  average high temperature per month in Fairbanks, Alaska
#

from matplotlib import pyplot

# Average high temperatures
january = 1.1
february = 10.0
march = 25.4
april = 44.5
may = 61.0
june = 71.6
july = 72.7
august = 65.9
september = 54.6
october = 31.9
november = 10.9
december = 4.8

# Plot the temperature for each month. 
pyplot.bar(1, january)
pyplot.bar(2, february)
pyplot.bar(3, march)
pyplot.bar(4, april)
pyplot.bar(5, may)
pyplot.bar(6, june)
pyplot.bar(7, july)
pyplot.bar(8, august)
pyplot.bar(9, september)
pyplot.bar(10, october)
pyplot.bar(11, november)
pyplot.bar(12, december)

# Draw a line across the graph for 32 degrees Fahrenheit
pyplot.plot([0, 14], [32, 32], "--")

# Format the graph and display it.
pyplot.title("Average high (F)")
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")
pyplot.xticks([1.4, 2.4, 3.4, 4.4, 5.4, 6.4, 7.4, 8.4, 9.4, 10.4, 11.4, 12.4], 
      ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

pyplot.show()

