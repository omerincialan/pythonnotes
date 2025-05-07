##
#  This program computes permutations of a string.
#

def main() :
   for string in permutations("eat") :
      print(string)

## Gets all permutations of a given word.
#  @param word the string to permute
#  @return a list of all permutations
#
def permutations(word) :
   result = []

   # The empty string has a single permutation: itself.
   if len(word) == 0 :
      result.append(word)
      return result
   else :
      # Loop through all character positions.
      for i in range(len(word)) :
         # Form a shorter word by removing the ith character.
         shorter = word[ : i] + word[i + 1 :]

         # Generate all permutations of the simpler word.
         shorterPermutations = permutations(shorter)

         # Add the removed character to the front of each permutation 
         # of the simpler word. 
         for string in shorterPermutations :
            result.append(word[i] + string)

      # Return all permutations.
      return result

# Start the program.
main()

