##
#  This program simulates a stamp machine that receives dollar bills and 
#  dispenses first class and penny stamps.
#

# Define the price of a stamp in pennies.
FIRST_CLASS_STAMP_PRICE = 49  

# Obtain the number of dollars.
dollarStr = input("Enter number of dollars: ")
dollars = int(dollarStr)

# Compute and print the number of stamps to dispense.
firstClassStamps = 100 * dollars // FIRST_CLASS_STAMP_PRICE
change = 100 * dollars - firstClassStamps * FIRST_CLASS_STAMP_PRICE
print("First class stamps: %6d" % firstClassStamps)
print("Penny stamps:       %6d" % change)

