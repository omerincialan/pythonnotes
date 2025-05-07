##
#  The selectionSort function sorts a list using the selection sort algorithm.
#

## Sorts a list, using selection sort.
#  @param values the list to sort
#
def selectionSort(values) :
   for i in range(len(values)) :
      minPos = minimumPosition(values, i)
      temp = values[minPos]  # swap the two elements
      values[minPos] = values[i]
      values[i] = temp

## Finds the smallest element in a tail range of the list.
#  @param values the list to sort
#  @param start the first position in values to compare
#  @return the position of the smallest element in the
#  range values[start] . . . values[len(values) - 1]
#
def minimumPosition(values, start) :
   minPos = start
   for i in range(start + 1, len(values)) :
      if values[i] < values[minPos] :
         minPos = i
         
   return minPos

