##
#  This program reads numerical exam grades from the user and produces a grade 
#  distribution histogram.
#

from matplotlib import pyplot

# Initialize the variables used to maintain the grade counts.
numAs = 0
numBs = 0
numCs = 0
numDs = 0
numFs = 0

# Use a while loop with a priming read to obtain the exam grades.
grade = int(input("Enter exam grade or -1 to finish: "))
while grade >= 0 :
   if grade >= 90.0 :
      numAs = numAs + 1
   elif grade >= 80.0 :
      numBs = numBs + 1
   elif grade >= 70.0 :
      numCs = numCs + 1
   elif grade >= 60.0 :
      numDs = numDs + 1
   else :
      numFs = numFs + 1
    
   grade = int(input("Enter exam grade or -1 to finish: "))
  
# Plot the grade distribution.
pyplot.bar(1, numAs)
pyplot.bar(2, numBs)
pyplot.bar(3, numCs)
pyplot.bar(4, numDs) 
pyplot.bar(5, numFs) 

# Add axis labels.
pyplot.xlabel("Grades")
pyplot.ylabel("Number of Students")

# Add a title that indicates the total number of students.
numStudents = numAs + numBs + numCs + numDs + numFs
pyplot.title("%d students\nGrade Distribution" % numStudents)

# Add the letter grades as labels under the bars.
pyplot.xticks([1.4, 2.4, 3.4, 4.4, 5.4], ["A", "B", "C", "D", "F"])

# Display the graph.
pyplot.show()

