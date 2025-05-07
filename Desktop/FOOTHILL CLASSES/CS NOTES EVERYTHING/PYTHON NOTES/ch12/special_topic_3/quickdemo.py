##
#  This program demonstrates the quick sort algorithm by sorting a list
#  that is filled with random numbers.
#

from random import randint
from quicksort import quickSort

n = 20
values = []
for i in range(n) :
   values.append(randint(1, 100))   

print(values)
quickSort(values, 0, n - 1)
print(values)

