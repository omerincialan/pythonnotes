## 
#  This program translates a single line of text from text messaging 
#  abbreviations to English.
#

def main() :
   transMap = buildMapping("textabbv.txt")
   
   print("Enter a message to be translated:")
   message = input("")
   theParts = message.split()
   
   translation = ""
   for abbrv in theParts :
      translation = translation + translateAbbrv(transMap, abbrv) + " "
      
   print("The translated text is:")
   print(translation)
      
## Extracts abbreviations and their corresponding English phrases from a 
#  file and builds a translation mapping.
#  @param filename name of the file containing the translations
#  @return a dictionary associating abbreviations with phrases
#
def buildMapping(filename) :
   transMap = {}
   infile = open(filename, "r")
   for line in infile :
      parts = line.split(":")
      transMap[parts[0]] = parts[1].rstrip()
      
   infile.close()
   return transMap

## Translates a single abbreviation using the translation map. If the abbre-
#  viation ends with a punctuation mark, it remains part of the translation. 
#  @param transMap a dictionary containing the common translations
#  @param abbrv a string that contains the abbreviation to be translated
#  @return the word or phrase corresponding to the abbreviation. If the
#  abbreviation cannot be translated, it is returned unchanged 
#
def translateAbbrv(transMap, abbrv) :
   # Determine if the word ends with a punctuation mark.
   lastChar = abbrv[len(abbrv) - 1]
   if lastChar in ".?!,;:" :
      abbrv = abbrv.rstrip(lastChar)
   else :
      lastChar = ""

   # Translate the abbrv.
   if abbrv in transMap :
      word = transMap[abbrv]
   else :
      word = abbrv
      
   # Return the translated word and the original punctuation mark.
   return word + lastChar

# Start the program.
main()

