##
#  The shellSort function sorts a list, using the Shell sort algorithm.
#

## Sorts a list, using Shell sort.
#  @param values the list to sort
#
def shellSort(values) :
   # Generate the sequence values.
   columns = []
   c = 1
   while c < len(values) :
      columns.append(c)
      c = 3 * c + 1

   # For each column count, sort all columns.
   s = len(columns) - 1
   while s >= 0 :
      c = columns[s]
      for k in range(c) :
         insertionSort(values, k, c)         
      s = s - 1

## Sorts a column, using insertion sort.
#  @param values the list to sort
#  @param k the index of the first element in the column
#  @param c the gap between elements in the column
#
def insertionSort(values, k, c) :
   i = k + c
   while i < len(values) :
      nextValue = values[i]
      # Move all larger elements up.
      j = i
      while j >= c and values[j - c] > nextValue :
         values[j] = values[j - c]
         j = j - c
         
      # Insert the element.
      values[j] = nextValue
      i = i + c

