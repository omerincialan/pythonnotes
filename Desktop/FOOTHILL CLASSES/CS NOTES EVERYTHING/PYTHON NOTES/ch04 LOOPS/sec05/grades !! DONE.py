##
#  This program computes information related to a sequence of grades obtained
#  from the user. It computes the number of passing and failing grades, 
#  computes the average grade and finds the highest and lowest grade.
#

# Initialize the counter variables.
numPassing = 0
numFailing = 0

# Initialize the variables used to compute the average.
total = 0
count = 0

# Initialize the min and max variables.
minGrade = 100.0        # Assuming 100 is the highest grade possible.
maxGrade = 0.0

# Use a while loop with a priming read to obtain the grades.
grade = float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0 :
   # Increment the passing or failing counter.
   if grade >= 60.0 :
      numPassing = numPassing + 1
   else :
      numFailing = numFailing + 1
      
   # Determine if the grade is the min or max grade.
   if grade < minGrade :
      minGrade = grade
   if grade > maxGrade :
      maxGrade = grade
      
   # Add the grade to the running total.
   total = total + grade
   count = count + 1
      
   # Read the next grade.
   grade = float(input("Enter a grade or -1 to finish: ")) 

# Print the results.
if count > 0 :
   average = total / count
   print("The average grade is %.2f" % average)
   print("Number of passing grades is", numPassing)
   print("Number of failing grades is", numFailing)
   print("The maximum grade is %.2f" % maxGrade)
   print("The minimum grade is %.2f" % minGrade)

