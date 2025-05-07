##
#  This program demonstrates the insertion sort algorithm.
#

from random import randint
from insertionsort import insertionSort

n = 20
values = []
for i in range(n) :
   values.append(randint(1, 100))   

print(values)
insertionSort(values)
print(values)

