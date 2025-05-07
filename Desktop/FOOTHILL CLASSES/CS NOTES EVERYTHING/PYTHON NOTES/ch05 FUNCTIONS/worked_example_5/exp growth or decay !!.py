##
# This program creates bar charts to illustrate exponential growth or
# decay over long periods of time.
#

from matplotlib import pyplot

def main() :
   showGrowthChart(1000.0, 1.0, 500, 50, "Bank balance")
   showGrowthChart(100.0, -0.0121, 6000, 500, "Carbon decay")


## Constructs a bar chart that shows the cumulative increase or 
#  decrease in a quantity over many years.
#  @param initial (float) the initial value of the quantity
#  @param rate (float) the percentage rate of change per year 
#  @param years (int) the number of years to show in the chart
#  @param bardistance (int) the number of years between successive bars
#  @param title (string) the title of the graph
#
def showGrowthChart(initial, rate, years, bardistance, title) :
  
   amount = initial
   bar = 0 

   # Add the bar for the initial amount.
   pyplot.bar(bar, amount, align = "center")
   bar = bar + 1

   year = 1
   while year <= years :
      # Update the amount
      change = amount * rate / 100
      amount = amount + change
      # If a bar should be drawn for this year, draw it
      if year % bardistance == 0 :    
         pyplot.bar(bar, amount, align = "center")
         bar = bar + 1
      year = year + 1

   # Set the title of the chart
   if rate >= 0 :
      subtitle = "Growth rate %.4f percent" % rate
   else :
      subtitle = "Decay rate %.4f percent" % -rate

   pyplot.title(title + "\n" + subtitle)

   # Configure the axes
   pyplot.xlabel("Year")
   pyplot.ylabel("Amount")
   pyplot.xticks(range(0, bar), range(0, year, bardistance))

   # Fit the plot area tightly around the bar chart. 
   pyplot.xlim(-0.5, bar - 0.5)

   pyplot.show()
    
main()

