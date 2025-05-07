##
#  This program computes an estimate of pi by simulating 
#  dart throws onto a square.
#

from random import random

TRIES = 10000

hits = 0
for i in range(TRIES) :

   # Generate two random numbers between -1 and 1   
   r = random()
   x = -1 + 2 * r 
   r = random()
   y = -1 + 2 * r         

   # Check whether the point lies in the unit circle   
   if x * x + y * y <= 1 :
      hits = hits + 1
    
# The ratio hits / tries is approximately the same as the ratio 
# circle area / square area = pi / 4.

piEstimate = 4.0 * hits / TRIES
print("Estimate for pi:", piEstimate)

