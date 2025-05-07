## 
#  This program illustrates the recursive digitSum function.
#

def main() :
   print("Digit sum:",  digitSum(1729))
   print("Expected: 19")
   print("Digit sum:", digitSum(1000))
   print("Expected: 1")
   print("Digit sum:", digitSum(9))
   print("Expected: 9")
   print("Digit sum:", digitSum(0))
   print("Expected: 0")

## Computes the sum of the digits of a number.
#  @param n an integer >= 0
#  @return the sum of the digits of n  
#
def digitSum(n) :
   if n == 0 : return 0   # Special case for terminating the recursion
   return digitSum(n // 10) + n % 10  # General case

# Start the program.
main()

