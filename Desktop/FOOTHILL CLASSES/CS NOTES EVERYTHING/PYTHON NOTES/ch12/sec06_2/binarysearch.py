## 
#  This module implements a function for executing binary searches in a list.
#

## Finds a value in a range of a sorted list, using the binary search algorithm.
#  @param values the list in which to search
#  @param low the low index of the range
#  @param high the high index of the range
#  @param target the value to find
#  @return the index at which the target occurs, or -1 if it does not 
#  occur in the list
#
def binarySearch(values, low, high, target) :
   if low <= high :
      mid = (low + high) // 2
      
      if values[mid] == target :
         return mid
      elif values[mid] < target :
         return binarySearch(values, mid + 1, high, target)
      else :
         return binarySearch(values, low, mid - 1, target)
         
   else :
      return -1

