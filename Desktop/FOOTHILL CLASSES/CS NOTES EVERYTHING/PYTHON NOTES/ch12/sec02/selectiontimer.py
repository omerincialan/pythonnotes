##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the selection sort algorithm.
#

from random import randint
from selectionsort import selectionSort
from time import time

firstSize = int(input("Enter first list size: "))
numberOfLists = int(input("Enter number of lists: "))

for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   values = []
   # Construct random list.
   for i in range(size) :
      values.append(randint(1, 100))   

   startTime = time()
   selectionSort(values)
   endTime = time()
      
   print("Size: %d Elapsed time: %.3f seconds" % (size, endTime - startTime))

