##
#  This module implements a function for executing linear searches in a list.
#

## Finds a value in a list, using the linear search algorithm.
#  @param values the list to search
#  @param target the value to find
#  @return the index at which the target occurs, or -1 if it does not 
#  occur in the list
#
def linearSearch(values, target) :
   for i in range(len(values)) :
      if values[i] == target :
         return i
         
   return -1

