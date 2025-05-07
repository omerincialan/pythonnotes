##
#  This program reads four letter grades, entered one per line, and  
#  and displays the corresponding average grade. 
#
def main() :
   done = False
   while not done :
      done = processGradeSet()
 
## Processes one student's set of grades.
#  @return True if the sentinel was encountered or False otherwise
# 
def processGradeSet() :
   # Read the first grade.
   grade1 = input("Enter the first grade or Q to quit: ")
   if grade1.upper() == "Q" :
      return True
      
   # Read the next three grades.
   grade2 = input("Enter the second grade: ")
   grade3 = input("Enter the third grade: ")
   grade4 = input("Enter the fourth grade: ")
   
   # Compute and print their average.
   x1 = gradeToNumber(grade1)
   x2 = gradeToNumber(grade2)
   x3 = gradeToNumber(grade3)
   x4 = gradeToNumber(grade4)
   xlow = min(x1, x2, x3, x4)
   avg = (x1 + x2 + x3 + x4 - xlow) / 3
   print(numberToGrade(avg))
   
   return False
   
## Converts a letter grade to a number.
#  @param grade a letter grade (A+, A, A-, . . ., D-, F)
#  @return the equivalent number grade
#
def gradeToNumber(grade) :
   result = 0
   first = grade[0]
   first = first.upper()
   if first == "A" :
      result = 4
   elif first == "B" :
      result = 3
   elif first == "C" :
      result = 2
   elif first == "D" :
      result = 1
      
   if len(grade) > 1 :
      second = grade[1]
      if second == "+" :
         result = result + 0.3
      elif second == "-" :
         result = result - 0.3
         
   return result
      
## Converts a number to the nearest letter grade.
#  @param x a number between 0 and 4.3
#  @return the nearest letter grade
#
def numberToGrade(x) :
   if x >= 4.15 : return "A+"
   if x >= 3.85 : return "A"
   if x >= 3.5 : return "A-"
   if x >= 3.15 : return "B+"
   if x >= 2.85 : return "B"
   if x >= 2.5 : return "B-"
   if x >= 2.15 : return "C+"
   if x >= 1.85 : return "C"
   if x >= 1.5 : return "C-"
   if x >= 1.15 : return "D+"
   if x >= 0.85 : return "D"
   if x >= 0.5 : return "D-"
   return "F"
   
# Start the program.
main()

