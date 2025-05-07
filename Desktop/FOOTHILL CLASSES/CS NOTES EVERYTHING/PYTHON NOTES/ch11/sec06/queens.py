##
#  This program solves the eight queens problem using backtracking.
#

def main() :
   solve([])

COLUMNS = "abcdefgh"
NQUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3

## Prints all solutions to the problem that can be extended from 
#  a given partial solution.
#  @param partialSolution the partial solution
#
def solve(partialSolution) :
   exam = examine(partialSolution)
   if exam == ACCEPT :
      print(partialSolution)
   elif exam != ABANDON :
      for p in extend(partialSolution) :
         solve(p)

## Examines a partial solution.
#  @param partialSolution the partial solution
#  @return ACCEPT if it is a complete solution, ABANDON if it is invalid,
#  or CONTINUE otherwise
#
def examine(partialSolution) :   
   for i in range(0, len(partialSolution)) :
      for j in range(i + 1, len(partialSolution)) :
         if attacks(partialSolution[i], partialSolution[j]) :
            return ABANDON
   if len(partialSolution) == NQUEENS :
      return ACCEPT
   else :
      return CONTINUE

## Checks whether one position attacks another. Positions are given as
#  strings with a letter for the column and a number for the row.
#  @param p1 a position
#  @param p2 another position
#  @return True if the positions are in the same row, column, or diagonal
#
def attacks(p1, p2) :
   column1 = COLUMNS.index(p1[0]) + 1
   row1 = int(p1[1])
   column2 = COLUMNS.index(p2[0]) + 1
   row2 = int(p2[1])
   return (row1 == row2 or column1 == column2 or 
      abs(row1 - row2) == abs(column1 - column2))

## Extends a partial solution to the next column.
#  @param partialSolution a partial solution to the problem
#  @return a list of all partial solutions that have a queen added in the
#  next column
#
def extend(partialSolution) :
   results = []
   row = len(partialSolution) + 1
   for column in COLUMNS :
      newSolution = list(partialSolution)
      newSolution.append(column + str(row))
      results.append(newSolution)
   return results
         
# Start the program.
main()

