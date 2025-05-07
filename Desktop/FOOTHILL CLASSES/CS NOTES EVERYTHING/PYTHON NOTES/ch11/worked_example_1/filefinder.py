##
#  This program lists all Python files in a directory and its subdirectories.
#

from os import listdir
from os.path import isdir, join

def main() :
#  startingDirectory = "/home/myname/pythonforeveryone"
   startingDirectory = "/home/necaise/books/pfe3private/code"
   find(startingDirectory, ".py")

## Prints all files whose names end in a given extension.
#  @param dir the starting directory
#  @param extension a file extension (such as ".py")
#
def find(dir, extension) :
   for f in listdir(dir) :
      child = join(dir, f)
      if isdir(child) :
         find(child, extension)
      elif child.endswith(extension) :
         print(child)

# Start the program.
main()

