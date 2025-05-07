##
#  This program computes a final score for a series of quiz scores: the sum 
#  after dropping the two lowest scores. The program uses a list.
#

def main() :
   scores = readFloats()
   if len(scores) > 1 :
      removeMinimum(scores)
      removeMinimum(scores)
      total = sum(scores)
      print("Final score:", total)      
   else :
      print("At least two scores are required.")

## Reads a sequence of floating-point numbers.
#  @return a list containing the numbers
#
def readFloats() :
   # Create an empty list.
   values = []
   
   # Read the input values into a list.
   print("Please enter values, Q to quit:")
   userInput = input("")
   while userInput.upper() != "Q" :
      values.append(float(userInput))
      userInput = input("")
      
   return values

## Removes the minimum value from a list.
#  @param values a list of size >= 1
#
def removeMinimum(values) :
   smallestPosition = 0
   for i in range(1, len(values)) :
      if values[i] < values[smallestPosition] :
         smallestPosition = i
         
   values.pop(smallestPosition)
   
# Start the program.
main()

