##
#  This program prints a table showing the world population growth over 300 
#  years.
#

ROWS = 6
COLUMNS = 7

# Initialize the populations table.
populations = [
      [ 106, 107, 111, 133, 221, 767, 1766 ],
      [ 502, 635, 809, 947, 1402, 3634, 5268 ],
      [ 2, 2, 2, 6, 13, 30, 46 ],
      [ 163, 203, 276, 408, 547, 729, 628 ],
      [ 2, 7, 26, 82, 172, 307, 392 ],
      [ 16, 24, 38, 74, 167, 511, 809 ]
    ]

# Define a list of continent names.
continents = [
     "Africa",
     "Asia",
     "Australia",
     "Europe",
     "North America",
     "South America"
   ]

# Print the table header.
print("                Year 1750 1800 1850 1900 1950 2000 2050")
      
# Print population data.
for i in range(ROWS) :
   # Print the ith row
   print("%20s" % continents[i], end="")
   for j in range(COLUMNS) :
      print("%5d" % populations[i][j], end="")

   print()  # Start a new line at the end of the row.      
      
# Print column totals.
print("               World", end="")
for j in range(COLUMNS) :
   total = 0
   for i in range(ROWS) :
      total = total + populations[i][j]
   
   print("%5d" % total, end="")

print()

