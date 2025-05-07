##
# This program constructs a bubble chart that illustrates the relationship 
# between annual education spending and math and science test scores.  
#

from matplotlib import pyplot

# Load the data from the text file.
infile = open("education.txt")
countries = []
mathScores = []
sciScores = []
spending = []

done = False
while not done :
   country = infile.readline()
   if country == "" :
      done = True
   else :
      line = infile.readline()
      countries.append(country)
      parts = line.split()
      
      dollars = int(parts[0])
      math = int(parts[1])
      science = int(parts[2])
  
      # Scaling the bubbles so that they don't overlap
      spending.append(dollars / 10) 
      mathScores.append(math)
      sciScores.append(science)  
      
infile.close()

# Construct the bubble chart.
pyplot.scatter(mathScores, sciScores, spending, 
   range(0, len(countries)))

# Label each bubble.
for i in range(len(countries)) :
   pyplot.text(mathScores[i], sciScores[i], 
      countries[i], color="gray")

pyplot.grid("on")
pyplot.xlabel("Math Test Scores (600 possible)")
pyplot.ylabel("Science Test Scores (600 possible)")
pyplot.title("Math Scores vs Science Scores vs Education Spending")

pyplot.show()

