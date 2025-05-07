## 
#  This program solves the Towers of Hanoi puzzle.
#

def main() :
   NDISKS = 5
   disks = []
   for i in range(NDISKS, 0, -1) :
      disks.append(i)
   towers = [disks, [], []]
   move(towers, NDISKS, 0, 2)

## Moves a pile of disks from one peg to another and displays the movement.
#  @param towers a list of three lists of disks
#  @param disks the number of disks to move
#  @param fromPeg the peg from which to move the disks
#  @param toPeg the peg to which to move the disks
#
def move(towers, disks, fromPeg, toPeg) :
   if disks > 0 :
      other = 3 - fromPeg - toPeg
      move(towers, disks - 1, fromPeg, other)
      diskToMove = towers[fromPeg].pop()
      towers[toPeg].append(diskToMove)
      print(towers)
      move(towers, disks - 1, other, toPeg)

# Start the program.
main()

