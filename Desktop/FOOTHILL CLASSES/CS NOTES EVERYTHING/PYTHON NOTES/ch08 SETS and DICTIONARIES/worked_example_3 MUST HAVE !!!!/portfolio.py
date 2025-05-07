##
#  This module defines functions for working with category allocations in a 
#  stock portfolio.
#

## Loads the category allocations from a stock portfolio.
#  @param filename name of the file containing the portfolio
#  @return a dictionary consisting of category codes and total per category
#
def loadAllocations(filename) :
   # Open the stock portfolio file.
   infile = open("stocks.txt", "r")
   
   # Extract the stocks and accumulate the category sums.
   allocations = {}
   for line in infile :
      fields = line.split()
      cat = fields[1]
      amount = float(fields[2])
      if cat in allocations :
         allocations[cat] = allocations[cat] + amount
      else :
         allocations[cat] = amount
      
   infile.close()
   return allocations         

## Builds a list of dictionaries that contain the categories, allocation
#  percentages, and slice colors.
#  @param allocations a dictionary containing the stock allocations by category
#  @return a list of dictionaries containing the pie chart and legend information 
#
def buildChartData(allocations) :
   categories = [
      {"cat": "small", "color": "blue", "label": "Small Cap"},
      {"cat": "mid", "color": "red", "label": "Mid Cap"},
      {"cat": "large", "color": "green", "label": "Large Cap"}, 
      {"cat": "misc", "color": "magenta", "label": "Other"}, 
      {"cat": "cash", "color": "yellow", "label": "Cash"}
   ]
   
   # Compute the total allocations.
   total = sum(allocations.values())
      
   # Compute the percentages per category and build a list of categories.
   slices = []
   for info in categories :
      category = info["cat"]
      info["size"] = allocations[category] / total
      slices.append(info)
   
   return slices

