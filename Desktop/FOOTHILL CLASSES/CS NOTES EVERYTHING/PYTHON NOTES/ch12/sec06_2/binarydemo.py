##
#  This program demonstrates the binary search algorithm.
#

from random import randint
from binarysearch import binarySearch

# Construct a random sorted list
n = 20
values = [1]
for i in range(1, n) :
   values.append(values[i - 1] + randint(1, 3))   
print(values)

done = False
while not done :
   target = int(input("Enter number to search for, -1 to quit: "))
   if target == -1 :
      done = True
   else :
      pos = binarySearch(values, 0, len(values) - 1, target)
      if pos == -1 :
         print("Not found")
      else :
         print("Found in position ", pos) 

