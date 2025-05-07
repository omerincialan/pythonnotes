##
# This program prints the names of all GIF image files in the current directory
# and the subdirectories of the current directory.
#

import os

print("Image Files:")

# Get the contents of the current directory.
dirName = os.getcwd()
contents = os.listdir()
for name in contents :
   # If the entry is a directory, repeat on its contents.
   if os.path.isdir(name) :   
      for name2 in os.listdir(name) :
         entry = os.path.join(name, name2)
         # If it is a file ending in .gif, print it.
         if os.path.isfile(entry) and name2.endswith(".gif") :
            print(os.path.join(dirName, entry))
            
   # Otherwise, it's a file. If the name ends in .gif, print it.
   elif name.endswith(".gif") :
      print(os.path.join(dirName, name))

