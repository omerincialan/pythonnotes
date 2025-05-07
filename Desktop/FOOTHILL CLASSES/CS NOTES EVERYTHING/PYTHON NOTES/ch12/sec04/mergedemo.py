##
#  This program demonstrates the merge sort algorithm by
#  sorting a list that is filled with random numbers.
#

from random import randint
from mergesort import mergeSort

n = 20
values = []
for i in range(n) :
   values.append(randint(1, 100))   
print(values)
mergeSort(values)
print(values)

