## 
#  This program maintains a dictionary of name/phone number pairs.
#

def main() :
   myContacts = {"Fred": 7235591, "Mary": 3841212, 
                 "Bob": 3841212, "Sarah": 2213278 } 

   # See if Fred is in the list of contacts.
   if "Fred" in myContacts :
      print("Number for Fred:", myContacts["Fred"])
   else :
      print("Fred is not in my contact list.")
      
   # Get and print a list of every contact with a given number.
   nameList = findNames(myContacts, 3841212)         
   print("Names for 384-1212: ", end="")
   for name in nameList :
      print(name, end=" ")
   print()   
   
   # Print a list of all names and numbers.
   printAll(myContacts)

## Find all names associated with a given telephone number.
#  @param contacts the dictionary
#  @param number the telephone number to be searched
#  @return the list of names
#
def findNames(contacts, number) :
   nameList = []
   for name in contacts :
      if contacts[name] == number :
         nameList.append(name)
                            
   return nameList

## Print an alphabetical listing of all dictionary items.
#  @param contacts the dictionary
#
def printAll(contacts) :
   print("All names and numbers:")
   for key in sorted(contacts) :
      print("%-10s %d" % (key, contacts[key]))
   
# Start the program.
main()

