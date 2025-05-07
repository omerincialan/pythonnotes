##
#  This program computes Fibonacci numbers using an iterative function.
#

def main() :
   n = int(input("Enter n: "))
   for i in range(1, n + 1) :
      f = fib(i)
      print("fib(%d) = %d" % (i, f))

## Computes a Fibonacci number.
#  @param n an integer
#  @return the nth Fibonacci number
#
def fib(n) :
   if n <= 2 :
      return 1
   else :
      olderValue = 1
      oldValue = 1
      newValue = 1
      for i in range(3, n + 1) :
         newValue = oldValue + olderValue
         olderValue = oldValue
         oldValue = newValue
         
      return newValue
      
# Start the program.
main()

