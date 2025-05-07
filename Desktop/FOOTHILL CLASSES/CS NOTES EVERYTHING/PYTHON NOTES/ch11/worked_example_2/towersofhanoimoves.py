##
#   This program prints instructions for solving a Towers of Hanoi puzzle.
#

def main() :
   move(5, 1, 3)
   
## Print instructions for moving a pile of disks from one peg to another.
#  @param disks the number of disks to move
#  @param fromPeg the peg from which to move the disks
#  @param toPeg the peg to which to move the disks
#
def move(disks, fromPeg, toPeg) :
   if disks > 0 :
      other = 6 - fromPeg - toPeg
      move(disks - 1, fromPeg, other)
      print("Move disk from peg", fromPeg, "to", toPeg)
      move(disks - 1, other, toPeg)
      
# Start the program.
main()

