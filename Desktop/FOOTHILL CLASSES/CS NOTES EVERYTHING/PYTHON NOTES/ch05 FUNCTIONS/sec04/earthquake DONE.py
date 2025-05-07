## 
#  This program gives a description of an earthquake, given the Richter scale 
#  magnitude.
#

def main() :
   # Extract the user input.
   richter = float(input("Enter a magnitude on the Richter scale: "))
 
   # Get the description and print it.
   description = getDescription(richter)
   print(description)
   
## Gets the description of an earthquake for a given magnitude 
#  on the Richter scale.
#  @param richter a float indicating the magnitude on the Richter scale
#  @return a string containing the description of the damage
#
def getDescription(richter) :
   if richter >= 8.0 :
     result = "Most structures fall"
   elif richter >= 7.0 :
     result = "Many buildings destroyed"
   elif richter >= 6.0 :
     result = "Many buildings considerably damaged, some collapse"
   elif richter >= 4.5 :
     result = "Damage to poorly constructed buildings"
   else : 
     result = "No destruction of buildings"
     
   return result
 
## Gets the description of an earthquake for a given magnitude on the Richter
#  scale. This implementation uses a shorter form of the if statement 
#  (see Special Topic 5.1)
#  @param richter a float indicating the magnitude on the Richter scale
#  @return a string containing the description of the damage
#
def getDescription2(richter) :
   if richter >= 8.0 : return "Most structures fall"
   if richter >= 7.0 : return "Many buildings destroyed"
   if richter >= 6.0 : return "Many buildings considerably damaged, some collapse"
   if richter >= 4.5 : return "Damage to poorly constructed buildings"
   return "No destruction of buildings"

# Start the program.
main()

