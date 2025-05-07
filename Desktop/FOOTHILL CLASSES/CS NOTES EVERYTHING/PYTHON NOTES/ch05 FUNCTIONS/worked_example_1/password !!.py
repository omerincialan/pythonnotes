##
#  This program generates a random password.
#

from random import randint

def main() :
   result = makePassword(8)
   print(result)
   
## Generates a random password.
#  @param length an integer that specifies the length of the password
#  @return a string containing the password of the given length with one digit 
#  and one special character
def makePassword(length) :
   password = ""
   
   # Pick random letters.
   for i in range(length - 2) :
      password = password + randomCharacter("abcdefghijklmnopqrstuvwxyz")
 
   # Insert a random digit and a random special character.
   randomDigit = randomCharacter("0123456789")
   password = insertAtRandom(password, randomDigit)
 
   randomSymbol = randomCharacter("+-*/?!@#$%&")
   password = insertAtRandom(password, randomSymbol)
 
   return password

## Returns a string containing one character randomly chosen from a given string.
#  @param characters the string from which to randomly choose a character
#  @return a substring of length 1, taken at a random index
#
def randomCharacter(characters) :
   n = len(characters)
   r = randint(0, n - 1)
   return characters[r] 

## Inserts one string into another at a random position.
#  @param string the string into which another string is inserted
#  @param toInsert the string to be inserted
#  @return the string that results from inserting toInsert into string
#
def insertAtRandom(string, toInsert) :   
   n = len(string)
   r = randint(0, n)
   result = ""

   for i in range(r) :
      result = result + string[i]
   result = result + toInsert
   for i in range(r, n) :
      result = result + string[i]
   
   return result
 
# Start the program.
main()

