##
#  This program demonstrates the various string methods that test substrings.
#

# Obtain a string and substring from the user.
theString = input("Enter a string: ")
theSubString = input("Enter a substring: ")

if theSubString in theString :
   print("The string does contain the substring.")

   howMany = theString.count(theSubString)
   print("   It contains", howMany, "instance(s)")
   
   where = theString.find(theSubString)
   print("   The first occurrence starts at position", where)
   
   if theString.startswith(theSubString) :
      print("   The string starts with the substring.")
   else :
      print("   The string does not start with the substring.")
      
   if theString.endswith(theSubString) :
      print("   The string ends with the substring.")
   else :
      print("   The string does not end with the substring.")      
   
else :
   print("The string does not contain the substring.")

