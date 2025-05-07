##
#  This program uses a loop to determine if a string is a palindrome.
#

def main() :
   sentence1 = "Madam, I'm Adam!"      
   print(sentence1)
   print("Palindrome:", isPalindrome(sentence1))
   sentence2 = "Sir, I'm Eve!"
   print(sentence2)
   print("Palindrome:", isPalindrome(sentence2))

## Tests whether a text is a palindrome.
#  @param text a string that is being checked
#  @return True if text is a palindrome, False otherwise
#
def isPalindrome(text) :
   start = 0
   end = len(text) - 1
   while start < end :
      first = text[start].lower()
      last = text[end].lower()
      if first.isalpha() and last.isalpha() :
         # Both are letters.
         if first == last :
            start = start + 1
            end = end - 1
         else :
            return False
            
      if not last.isalpha() :
         end = end - 1
         
      if not first.isalpha() :
         start = start + 1
         
   return True
   
# Start the program.
main()

