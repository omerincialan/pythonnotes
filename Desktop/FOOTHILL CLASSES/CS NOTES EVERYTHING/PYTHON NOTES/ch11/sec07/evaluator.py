## 
#  This program evaluates arithmetic expressions.
#

def main() :
   expr = input("Enter an expression: ")
   tokens = tokenize(expr)
   value = expression(tokens)
   print(expr + "=" + str(value))

## Breaks a string into tokens.
#  @param inputLine a string consisting of digits and symbols
#  @return a list of numbers (made from the digits of the input) and symbols
#
def tokenize(inputLine) :
   result = []
   i = 0
   while i < len(inputLine) :
      if inputLine[i].isdigit() :
         j = i + 1
         while j < len(inputLine) and inputLine[j].isdigit() :
            j = j + 1
         result.append(int(inputLine[i : j]))
         i = j
      else :
         result.append(inputLine[i])
         i = i + 1
   return result

## Evaluates the expression.
#  @param tokens the list of tokens to process
#  @return the value of the expression
#
def expression(tokens) :
   value = term(tokens)
   done = False
   while not done and len(tokens) > 0 :
      nextToken = tokens[0]
      if nextToken == "+" or nextToken == "-" :
         tokens.pop(0)  # Discard "+" or "-"
         value2 = term(tokens)
         if nextToken == "+" : 
            value = value + value2 
         else :
            value = value - value2
      else : 
         done = True
         
   return value

## Evaluates the next term found in the expression.
#  @param tokens the list of tokens to process
#  @return the value of the term
#
def term(tokens) :
   value = factor(tokens)
   done = False
   while not done and len(tokens) > 0:
      nextToken = tokens[0]
      if nextToken == "*" or nextToken == "/" :
         tokens.pop(0)
         value2 = factor(tokens)
         if nextToken == "*" :
            value = value * value2               
         else : 
            value = value / value2
      else : 
         done = True         
   
   return value

## Evaluates the next factor found in the expression.
#  @param tokens the list of tokens to process
#  @return the value of the factor
#
def factor(tokens) :
   nextToken = tokens.pop(0)
   if nextToken == "(" :
      value = expression(tokens)
      tokens.pop(0)  # Discard ")"
   else :
      value = nextToken
      
   return value

# Start the program.
main()

