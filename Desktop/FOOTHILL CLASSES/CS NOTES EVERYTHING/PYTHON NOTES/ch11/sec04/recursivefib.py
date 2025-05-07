##
#  This program computes Fibonacci numbers using a recursive function.
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
      return fib(n - 1) + fib(n - 2)
      
# Start the program.
main()

