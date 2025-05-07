##
#  This program demonstrates the linear search algorithm.
#

from random import randint
from linearsearch import linearSearch

# Construct random list.
n = 20
values = []
for i in range(n) :
   values.append(randint(1, 20))   
print(values)

done = False
while not done :
   target = int(input("Enter number to search for, -1 to quit: "))
   if target == -1 :
      done = True
   else :
      pos = linearSearch(values, target)
      if pos == -1 :
         print("Not found")
      else :
         print("Found in position", pos) 

