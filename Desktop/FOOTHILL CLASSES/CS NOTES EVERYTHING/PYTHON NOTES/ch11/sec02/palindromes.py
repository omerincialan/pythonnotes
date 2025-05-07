##
#  This program uses recursion to determine if a string is a palindrome.
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
   length = len(text)

   # Separate case for shortest strings. 
   if length <= 1 :
      return True
   else :
      # Get first and last characters, converted to lowercase. 
      first = text[0].lower()
      last = text[length - 1].lower()

      if first.isalpha() and last.isalpha() :
         # Both are letters. 
         if first == last :
            # Remove both first and last character. 
            shorter = text[1 : length - 1]
            return isPalindrome(shorter)
         else :            
            return False
      elif not last.isalpha() :
         # Remove last character. 
         shorter = text[0 : length - 1]
         return isPalindrome(shorter)
      else :
         # Remove first character. 
         shorter = text[1 : length]
         return isPalindrome(shorter)
         
# Start the program.
main()

