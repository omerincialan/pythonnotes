##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the Shell sort algorithm.
#

from random import randint
from time import time
from shellsort import shellSort
from quicksort import quickSort
from insertionsort import insertionSort

firstSize = int(input("Enter first list size: "))
numberOfLists = int(input("Enter number of lists: "))

for k in range(1, numberOfLists + 1) :
   size = firstSize * k
   values = []
   # Construct random list.
   for i in range(size) :
      values.append(randint(1, 100))   
   values2 = list(values)
   values3 = list(values)

   startTime = time()
   shellSort(values)
   endTime = time()
   shellTime = endTime -startTime

   startTime = time()
   quickSort(values2, 0, size - 1)
   endTime = time()
   quickTime = endTime -startTime

   for i in range(size) :
      if values[i] != values2[i] :
         raise RuntimeError("Incorrect sort result.") 
      
   startTime = time()
   insertionSort(values3)
   endTime = time()
   insertionTime = endTime -startTime

   print("Size: %d Shell sort: %.3f Quicksort: %.3f Insertion sort: %.3f seconds" 
         % (size, shellTime, quickTime, insertionTime))

