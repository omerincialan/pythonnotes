##
#  The sort function sorts a list, using the quicksort algorithm.
#

## Sorts a portion of a list, using quicksort.
#  @param values the list to sort
#  @param start the first index of the portion to be sorted
#  @param to the last index of the portion to be sorted
#
def quickSort(values, start, to) :
   if start >= to : return
   p = partition(values, start, to)
   quickSort(values, start, p)
   quickSort(values, p + 1, to)

## Partitions a portion of a list.
#  @param values the list to partition
#  @param start the first index of the portion to be partitioned
#  @param to the last index of the portion to be partitioned
#  @return the last index of the first partition
#
def partition(values, start, to) :
   pivot = values[start]
   i = start - 1
   j = to + 1
   while i < j :
      i = i + 1
      while values[i] < pivot :
         i = i + 1
      j = j - 1
      while values[j] > pivot :
         j = j - 1
      if i < j :
         temp = values[i] # Swap the two elements
         values[i] = values[j]
         values[j] = temp
   return j

