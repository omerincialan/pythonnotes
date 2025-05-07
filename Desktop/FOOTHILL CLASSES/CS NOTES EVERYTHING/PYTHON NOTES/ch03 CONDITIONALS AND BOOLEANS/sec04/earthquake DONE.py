##
#  This program prints a description of an earthquake, given the Richter scale 
#  magnitude.
#

# Obtain the user input.
#richter = float(input("Enter a magnitude on the Richter scale: "))
richter = 5.00

# Print the description
if richter >= 8.0 :
   print("Most structures fall")
if richter >= 7.0 :
   print("Most structures severely damaged")

