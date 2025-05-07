##
#  This program demonstrates the selection sort algorithm by sorting a
#  list that is filled with random numbers.

from random import randint
from selectionsort import selectionSort 

n = 20
values = []
for i in range(n) :
   values.append(randint(1, 100))   
print(values)
selectionSort(values)
print(values)

