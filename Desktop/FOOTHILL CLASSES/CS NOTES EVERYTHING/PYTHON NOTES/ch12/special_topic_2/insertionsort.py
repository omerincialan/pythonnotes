## 
#  The insertionSort function sorts a list, using the insertion sort algorithm.
#

# Sorts a list, using insertion sort.
# @param values the list to sort
#
def insertionSort(values) :
   for i in range(1, len(values)) :
      nextValue = values[i]

      # Move all larger elements up.
      j = i
      while j > 0 and values[j - 1] > nextValue :
         values[j] = values[j - 1]
         j = j - 1
         
      # Insert the element
      values[j] = nextValue

