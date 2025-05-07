##
#  This program displays the most common baby names. Half of boys and girls in
#  the United States were given these names in 2011.
#

# The percentage limit to be extracted.
LIMIT = 50.0

def main() :
   inputFile = open("babynames.txt", "r")
   
   boyTotal = 0.0
   girlTotal = 0.0
   while boyTotal < LIMIT or girlTotal < LIMIT :      
      # Extract the data from the next line and split it.
      line = inputFile.readline()
      dataFields = line.split()

      # Extract the individual field values.
      rank = int(dataFields[0])
      boyName = dataFields[1]
      boyPercent = float(dataFields[2].rstrip("%"))
      girlName = dataFields[3]
      girlPercent = float(dataFields[4].rstrip("%"))
            
      # Process the data.            
      print("%3d " % rank, end="")
      boyTotal = processName(boyName, boyPercent, boyTotal)
      girlTotal = processName(girlName, girlPercent, girlTotal)
      print()
      
   inputFile.close()
   
## Prints the name if total < LIMIT and adjusts the total.
#  @param name the boy or girl name
#  @param percent the percentage for this name
#  @param total the total percentage processed
#  @return the adjusted total
#
def processName(name, percent, total) :
   if total < LIMIT :
      print("%-15s" % name, end="")
   else :
      print("%-15s" % "", end="")

   total = total + percent
   return total      
   
# Start the program.
main()

