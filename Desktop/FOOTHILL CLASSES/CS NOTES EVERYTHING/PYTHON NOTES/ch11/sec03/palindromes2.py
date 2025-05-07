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
   return substringIsPalindrome(text, 0, len(text) - 1)

## Recursively tests whether a substring is a palindrome.
#  @param text a string that is being checked
#  @param start the index of the first character of the substring
#  @param end the index of the last character of the substring
#  @return True if the substring is a palindrome
#
def substringIsPalindrome(text, start, end) :
   # Separate case for substrings of length 0 and 1.
   if start >= end :
      return True
   else :
      # Get first and last characters, converted to lowercase.
      first = text[start].lower()
      last = text[end].lower()
      if first.isalpha() and last.isalpha() :
         if first == last :
            # Test substring that doesn’t contain the matching letters.
            return substringIsPalindrome(text, start + 1, end - 1)
         else :
            return False
      elif not last.isalpha() :
         # Test substring that doesn’t contain the last character.
         return substringIsPalindrome(text, start, end - 1)
      else :
         # Test substring that doesn’t contain the first character.
         return substringIsPalindrome(text, start + 1, end)
         
# Start the program.
main()

